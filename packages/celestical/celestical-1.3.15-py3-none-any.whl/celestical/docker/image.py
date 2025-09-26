"""
This module contains classes related to docker images
"""
import gzip
import subprocess
from pathlib import Path
from tqdm import tqdm
import docker.errors

from celestical.config import Config
from celestical.utils.files import get_most_recent_file
from celestical.utils.display import print_text
from celestical.utils.prompts import confirm_user
from celestical.docker.docker import DockerMachine

class Image:
    """
        This class contains attributes and method to interact with a specific
        local docker image.
    """
    def __init__(self,
            config:Config = None,
        ) -> None:
        self.config = config
        if config is None:
            self.config = Config()

        self.docker = DockerMachine()

    def confirm_zip_path(self,
            image_name: str,
            project_name: str) -> (Path, Path):
        """Confirms with user whether to rezip or not if image zip file exists and updates
           gz_paths accordingly
        Params:
            images: string or list of strings of image full tag names
                    as they should appear in the "image" field of each service
            project_name: a string given to name the project, usually the base
                    domain name
        Returns:
            zipfile path
        """
        # --- preparing save directory
        save_path = Path(f"/tmp/celestical/{project_name}/")
        # Create the save_path directory and any necessary parent directories
        save_path.mkdir(parents=True, exist_ok=True)

        # --- preparing list of images, or of 1 image
        escaped_image_name = image_name.replace('/', '__')
        escaped_image_name = escaped_image_name.replace(':', '_-_')
        gz_filename = save_path / f'{escaped_image_name}.tar.gz'
        gz_filename_local = Path(f'{escaped_image_name}.tar.gz')

        if not gz_filename_local.is_file():
            gz_filename_local = None

        return gz_filename, gz_filename_local

    def compress_images(self,
                        images: str|list[str],
                        project_name: str
                        ) -> list[Path]:
        """Compress one or several Docker images. Checking if compressed file
        does not already exist.

        Params:
            images: string or list of strings of image full tag names
                    as they should appear in the "image" field of each service
            project_name: a string given to name the project, usually the base
                    domain name
        Returns:
            A list of path to gzipped images to be uploaded
        """
        gz_paths = []

        # --- Getting docker client
        client = self.docker.get_docker_client()
        if client is None:
            self.config.logger.debug("Docker client could not be found.")
            return gz_paths

        # --- preparing list of images, or of 1 image
        if isinstance(images, str):
            images = [images]

        # --- Compressing all images in different gzips
        for image_name in images:
            if self._process_single_image(image_name, project_name, client, gz_paths):
                continue

        return gz_paths

    def _process_single_image(self, image_name: str, project_name: str,
                             client, gz_paths: list) -> bool:
        """Process a single image for compression.

        Returns True if image was processed (existing file used or command line method),
        False if Docker client method should be used.
        """
        gz_filename, cwd_gz_filename = self.confirm_zip_path(
            image_name, project_name)

        if cwd_gz_filename is not None:
            gz_filename = get_most_recent_file(
                gz_filename, cwd_gz_filename)

        if gz_filename.exists():
            if not confirm_user(
                    f"[yellow]{image_name}[/yellow] already prepared,"
                    + f"\n\trenew and overwrite {gz_filename} ?",
                    default=False):
                # User wants to use existing compressed file
                print_text(f" * Ok, using ready file: {gz_filename}\n")
                gz_paths.append(gz_filename)
                return True

        # Step 1: Calculate the total size of the image
        print_text(f"Working on {image_name}...")
        img = self._get_docker_image(client, image_name)

        if img is None:
            # --- try with calling command line
            if self._try_command_line_export(image_name, gz_filename, gz_paths):
                return True

            msg = (
                f"Image {image_name} not found for: {project_name}. "
                "If this image is built in the compose file, please run "
                "'docker compose build' first."
            )
            print_text(msg, worry_level="ohno")
            self.config.logger.debug(msg)
            return True

        # --- Get the tar image and calculate its size
        self.config.logger.debug("Checking Image Size: %s", img)
        image_data = img.save(named=True)
        total_size = sum(len(chunk) for chunk in image_data)
        total_size_mb = total_size / (1024 * 1024)

        print_text(f"Image Tag Found: {image_name}"
                + f"\n\timage size: {total_size_mb:.2f} MB"
                + f"\n\tsaving in: {gz_filename.resolve().parents[0]}"
                + f"\n\tas file name: {gz_filename}")

        # --- Reset the image data iterator for creating the tar archive
        image_data = img.save(named=True)

        # Save the Docker image to a gzip file with a progress bar
        print_text(f"Exporting compressed image (gzip) to {gz_filename} ...")
        self._save_image_with_progress(image_data, gz_filename, total_size)

        gz_paths.append(gz_filename)
        print_text(f"[green]succesfully prepared[/green]: {gz_filename}")
        return False

    def _get_docker_image(self, client, image_name: str):
        """Get Docker image using client, with proper exception handling."""
        try:
            msg = "Using docker client to image.get: " + image_name
            self.config.logger.debug(msg)
            return client.images.get(image_name)
        except (docker.errors.ImageNotFound, docker.errors.APIError,
                docker.errors.DockerException) as e:
            self.config.logger.debug("Failed to get image: %s", e)
            return None

    def _try_command_line_export(self, image_name: str, gz_filename: Path,
                                gz_paths: list) -> bool:
        """Try to export image using command line docker save."""
        try:
            print_text(f"Exporting compressed image (gzip) to {gz_filename} ...")
            with subprocess.Popen(["docker", "save", image_name,
                "|", "gzip",
                ">", gz_filename.resolve()
                ]) as cmd:

                if cmd.returncode == 0:
                    gz_paths.append(gz_filename)
                    print_text(f"[green]succesfully prepared[/green]: {gz_filename}")
                    return True
        except (subprocess.SubprocessError, OSError) as e:
            print_text(f"Image {image_name} could not be prepared: {e}",
                    worry_level="ohno")

        return False

    def _save_image_with_progress(self, image_data, gz_filename: Path, total_size: int):
        """Save image data to gzip file with progress bar."""
        with gzip.open(gz_filename, 'wb') as gz_file:
            with tqdm(total=total_size,
                    unit='B',
                    unit_scale=True,
                    desc="exporting") as pbar:
                # Read, compress, and write data in chunks
                for chunk in image_data:
                    gz_file.write(chunk)
                    pbar.update(len(chunk))
