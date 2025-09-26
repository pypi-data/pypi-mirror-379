"""
This module contains class which does local and remote app management
"""
from pathlib import Path
import shutil
import base64

from celestical.user import User
from celestical.compose import Compose, Enricher
from celestical.config.config import Config
from celestical.utils.display import (
    cli_panel,
    print_text,
    write_app_row,
    print_console,
    print_feedback)
from celestical.utils.prompts import confirm_user
from celestical.utils.files import save_yaml
from celestical.utils.waiters import Spinner, ProgressBar
from celestical.utils.crypt import Cryptic
from celestical.api.exceptions import (
    UnauthorizedException,
    BadRequestException)
from celestical.api import ApiException
from celestical import api
from celestical.docker import Image





class App:
    """ This class consist of attributes and methods to manage local files of a
    specific app.

    By default this object would create a new App.
    Unless given a valid app ID.
    """

    def __init__(
            self,
            app_id: str = "",
            config: Config = None,
            force_sync: bool = True,
            domain_list: list | None = None,
            compose: Compose = None,
            user: User = None):
        """ An App contains a ecompose dictionary/file

        Parameters:
            - app_id: an App ID to set and load if given
            - force_sync: True to force synching with the web or False to work
              offline.
            - domain_list: list of strings of domains already locally synched
            - compose: Compose object to work with if empty, it will create a
              new one.
            - user: User object to make requests with. if empty it will load
              the current config.
        """
        # Config related topics
        self.config = config
        if self.config is None:
            self.config = Config()
        self.logger = self.config.logger

        self.domain_list = [] if domain_list is None else domain_list

        # other setups
        self.user = user
        if user is None:
            self.user = User()

        # App ID is saved here to link it to the API
        self.app_id = app_id

        # all information should be in the compose metadata
        # including the app id and url.
        self.compose = compose
        if compose is None:
            self.compose = Compose()

        if len(app_id) >= 32 or force_sync is True:
            if not self.sync():
                print_text("App could not be synced.",
                       worry_level="oops")

    def __str__(self) -> str:
        info = f"App ID: {self.app_id}\n"
        info += f"  - {len(self.compose.services)} services:\n"
        for serv in self.compose.services:
            info += f"      - {serv}"
        return info

    def _get_app_dir(self) -> Path:
        """ This function returns the path to enriched docker compose file
        given the app ID

        Return:
            - Path to the directory containing this app ecompose file
        """
        path = self.config.get_app_config_dir() / self.app_id
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _get_ecompose_path(self) -> Path:
        """One place to define the ecompose path

            Content of that file is managed by the Compose object
        """
        return self._get_app_dir() / "ecompose.yml"

    def set_as_active_app(self) -> None:
        """ This function sets the active app the one which user is currently
            working on.

        Parameters:
          - active_app_id:str: ID of the active app in string format.
        """
        path = self.config.get_active_app_id_path()
        path.write_text(data=self.app_id)

    def enrich(self, in_compose_path:Path) -> bool:
        """ This function commands and check enrichment process

            1. it checks which file is most recent from the app or the given
            user input (docker compose file)
            2. if the command line input file is older than the app ecompose
            then we continue to 4.
            3. Enrich the ecompose file
            4. Upload compose to get information about what to upload
            5. Upload images and anciliary information (confs)
        """
        # Get this app ecompose path even if not exist
        current_ecompose_path = self._get_ecompose_path()

        # Get None if the user input does not exist
        # or the detected most probable compose file if a folder is given
        user_compose_path = self.compose.define_compose_path(in_compose_path)

        if user_compose_path is None and not current_ecompose_path.is_file():
            print_text("We could not find a path to a compose file.",
                       worry_level="oops")
            return False

        # Setup which file has been selected
        selected_path = user_compose_path

        # --- Enricher
        enricher = Enricher(self.compose)
        self.compose = enricher.prepare(
            ecompose_path=current_ecompose_path,
            selected_path=selected_path)

        self.save_app()
        return True

    def read_app_ecompose(self) -> dict:
        """
        This function read the apps enriched ecompose file and returns it.

        Return:
            - ecompose content in dict format

        """
        ecompose_path = self._get_ecompose_path()
        ecompose_dict = self.compose.read_docker_compose(ecompose_path)
        return ecompose_dict

    def save_app(self) -> Path|None:
        """ This function saves the ecompose file when given ecompose dict with
        app id.

        Returns:
            - Path to enriched docker compose file
        """
        self.compose.ecompose["celestical"]["app_id"] = self.app_id
        ecomp_save = self.compose.ecompose.copy()

        if ecomp_save.get("celestical_secrets", None) is not None:
            del ecomp_save["celestical_secrets"]

        ecompose_path = self._get_ecompose_path()
        print_text(f"Saving app: {self.app_id}")

        return save_yaml(data=ecomp_save,
                         yml_file=ecompose_path,
                         cli_logger=self.config.logger)

    def check_app_status(self):
        """ Check with celestical cloud the status of the app.
        """
        # if user is logged in
        apiconf = self.user.get_api_with_auth()
        with api.ApiClient(apiconf) as api_client:
            app_api = api.AppApi(api_client)
            #api_response = app_api.get_user_apps_app_status_get()
            app_api.get_app_app_app_uuid_get_with_http_info(
                app_uuid=self.app_id)

    def sync(self) -> bool:
        """ Makes initial setup and Sync local and celestical cloud apps state.

        This function does:
             - creating folder structure
             - syncing with remote corresponding app if exists
        """
        # Make sure the base apps folder exist or make it.
        # already done:  apps_dir.mkdir(parents=True, exist_ok=True)

        if self.app_id == "":
            # To create a new app we need a base domain
            if len(self.compose.get("base_domain")) == 0:
                self.compose.init_ecompose()

            # no id no sync
            self.create()
        else:  # we retrieve app info
            saved_app = self._get_app_from_api()
            if saved_app is None:
                return False
            self.compose.init_ecompose(
                base_domain=saved_app.url,
                app_id=self.app_id)

        return True
        # Create dedicated app folder or make sure it is created
        #self.sync_apps()

    def _make_encrypted_compose_pack(self, deploy: bool = True) -> dict:
        """ Make a compose pack with encrypted ecompose

            app_id can be empty in the pack
            app_url must be fed with the right info
        """
        compose_pack = {}

        # Default values
        compose_pack["enriched_compose"] = None
        compose_pack["deploy"] = deploy
        compose_pack["app_id"] = self.app_id
        compose_pack["app_url"] = self.compose.get("base_domain")

        cryptic = Cryptic(config=self.config)

        # No need to Convert string to bytes for base64 encoder
        # enc_compose_data is already bytes with self.config.encoding
        enc_compose_data = cryptic.encryption(self.compose.ecompose)

        if enc_compose_data is None or len(enc_compose_data) == 0:
            print_text(worry_level="ohno",
                       text="Encryption Failed: "+self.app_id)
            return compose_pack

        # Generate base64 bytes stream from encrypted bytes
        encrypted_data = base64.b64encode(enc_compose_data)

        # Convert back to string for JSON Serialization
        encrypted_data = encrypted_data.decode(self.config.encoding)

        compose_pack["enriched_compose"] = encrypted_data

        return compose_pack

    def create(
            self) -> Path|None:
        """
        This function makes a record in celestical cloud and gets the app ID.
        creates folder structure and creates a basic enriched compose if none
        given.

        Returns:
            - Path to the enriched docker compose file
        """
        # --- Posting the body package for Compose file
        compose_pack = self._make_encrypted_compose_pack(deploy=False)

        # Early stop
        if compose_pack.get("enriched_compose", None) is None:
            self.logger.error("compose: won't upload empty data")
            return None

        # ENDPOINT CALL
        api_response = self.upload_compose(compose_pack)
        if api_response is None:
            self.logger.warning("compose: could not be uploaded")
            return None

        if len(api_response.id) == 0:
            self.logger.warning("App not created: no app id found from API.")
            print_text(
                "App could not be created, could not get API response",
                worry_level="ohno",
            )
            return None

        # at this point api_response is an App
        self.app_id = str(api_response.id)
        self.compose.set("status", "just-created")

        path = self.save_app()

        print_feedback("Initiated App with ID: "+self.app_id)

        return path

    def push(self) -> bool:
        """ Manages push of an app for deployment
           - compose update
           - image updates
        """
        # self.save_app()
        compose_pack = self._make_encrypted_compose_pack(deploy=True)

        api_response = self.upload_compose(compose_pack)

        if api_response is None:
            return False

        if self.app_id != str(api_response.id):
            print_text("Enriched compose could not be pushed correctly",
                worry_level="ohno")

        return self.upload_images()

    def _get_app_from_api(self) -> api.App | None:
        """ This function gets app info from the API

        Return:
            - dict of app info or None if failed
        """
        apiconf = self.config.api_configuration()
        with api.ApiClient(apiconf) as api_client:
            app_api = api.AppApi(api_client)
            try:
                return app_api.get_app_app_app_uuid_get(self.app_id)
            except UnauthorizedException:
                return None

    def upload_compose(self, compose_pack: dict):
        """ Update or create a composed application

        Parameters
          - compose_pack
        Returns:
          - api response
        """
        apiconf = self.user.get_api_with_auth()
        if apiconf is None:
            return None

        api_response = None
        with api.ApiClient(apiconf) as api_client:
            app_api = api.AppApi(api_client)

            try:
                # App creation with compose (possibly empty) upload
                self.logger.debug("Preparing compose info to post")
                compose_to_post = api.Compose.from_dict(compose_pack)
            except (TypeError, ValueError, AttributeError) as oops:
                print_text(">>> [red]Compose data is not serializable[/red]")
                self.logger.error(oops)
                return None

            try:
                self.logger.debug("Making compose info push request")
                # Calling for a response without HTTP info
                # So we directly get an App schema
                api_response = app_api.upload_compose_file_app_compose_post( \
                    compose_to_post)

            except UnauthorizedException as oops:
                # Let's try to relog again and relaunch that function
                print_text(">>> [red]Access not authorized for now[/red]")
                print_text(f"  - Check your email is verified: {self.user.username}")
                print_text("  - Make sure a payment method is installed")
                self.logger.error("ERROR in App.create(): ")
                self.logger.error(" > ERROR unauthorized posting of enriched compose file")
                self.logger.error(oops)
                return None

            except BadRequestException as oops:
                print_text(">>> [red]Bad request[/red] to upload your compose file.")
                if len(compose_pack.get("app_url", "")) == 0:
                    print_text("  - Your app does not have a base domain.",
                               worry_level="oops")
                return None

            except ApiException as oops:
                print_text(">>> [red]No connection[/red] yet possible to initiate your app.")
                print_text("  - Check your Internet connection")
                print_text("  - Login again")
                print_text("  - Update celestical command line; pip install -U celestical")
                self.logger.error("ERROR in App.create(): ")
                self.logger.error(" > ERROR during posting of the enriched compose file")
                self.logger.error(oops)
                return None

        if not isinstance(api_response, api.App):
            self.logger.error("API response is not an App.")
            msg = "Try to login again, your token might have expired.\n"
            msg += "--> [underline]celestical login[/underline]"
            cli_panel(msg)
            return None

        return api_response

    def upload_images(self) -> bool:
        """Upload the enriched compose file to the Celestical Cloud."""

        cli_panel("Now uploading your App's images to Celestical")

        e_compose = self.compose.ecompose
        if e_compose is None:
            return False

        # Build the compressed tar file for services images
        image_names = [
            e_compose["services"][service_name]["image"]
            for service_name in e_compose["services"]
        ]

        image_d = Image(config=self.config)

        # if "name" not in e_compose["celestical"]:
        #    self.logger.warning("Upload needs an APP name or domain")
        #    raise typer.Abort()

        image_paths = image_d.compress_images(
            images=image_names,
            project_name=e_compose["celestical"].get("name", "_no-name_"))

        # Upload images
        apiconf = self.user.get_api_with_auth()
        if apiconf is None:
            return False

        with api.ApiClient(apiconf) as api_client:
            app_api = api.AppApi(api_client)
            for ipath in image_paths:
                self._upload_one_image(app_api, ipath)

        return True

    def write_row(self, app_information: api.App):
        """ Print the basic app information """
        app_min_dict = {
            "url": app_information.url,
            "created_date": app_information.created_date,
            "id": app_information.id
            }

        print_console(write_app_row(app_min_dict,
                                    key=1))

    def delete_app(self):
        """ Delete the app which has the app_id"""
        # --- Retrieve app and delete
        app_information = self._get_app_from_api()

        if app_information is None:
            # Inform No app found
            print_text("No app found")
            self.logger.warning("No app found while delete app")
            return None

        # --- Acknowledgement on the selected app
        self.write_row(app_information)
        confirm_delete_app = confirm_user(
            "Do you want to [red]delete that app[/red]?",
            default=False)

        if confirm_delete_app is False:
            print_text("App not deleted")
            return None

        # --- Delete the ecompose folder
        msg = f"Deleting app {self.app_id}"
        self.logger.info(msg)

        app_path = self._get_app_dir()
        if app_path.is_dir():
            try:
                shutil.rmtree(app_path)
            except OSError as oops:
                msg = f"Issue: during app_dir  deletion {app_path}"
                self.logger.warning(msg)
                self.logger.warning(oops)

        # --- Delete the Database record
        delete_app_status = None

        apiconf = self.user.get_api_with_auth()
        if apiconf is None:
            self.logger.warning("App configuration not found")
            return delete_app_status

        try:
            with api.ApiClient(apiconf) as api_client:
                app_api = api.AppApi(api_client)
                # This endpoint returns nothing meaningful on success; avoid assignment
                app_api.delete_app_app_app_uuid_delete(self.app_id)
                delete_app_status = True
        except ApiException as oops:
            msg = f"Could not delete the app from api: {self.app_id}"
            self.logger.error(msg)
            self.logger.error(oops)

        print_feedback(f"App successfully deleted: {self.app_id}")
        return delete_app_status

    def _upload_one_image(self, app_api: api.AppApi, ipath: Path) -> None:
        """Read a compressed image file and upload it, showing progress."""
        spinner = Spinner()
        try:
            file_size = ipath.stat().st_size
            file_bytes = bytearray()
            with ProgressBar(total_bytes=file_size,
                             description=f"Reading {ipath.name}") as progress_bar:
                with ipath.open(mode="rb") as fdesc:
                    while True:
                        chunk = fdesc.read(1024 * 1024)
                        if not chunk:
                            break
                        file_bytes.extend(chunk)
                        progress_bar.advance(len(chunk))
                progress_bar.complete()

            upfile = (ipath.name, bytes(file_bytes))
            self.logger.debug("Making image upload request")

            loading_msg = f"your image {ipath.name} is uploading"
            spinner.start(loading_msg)

            upload_method = (
                app_api
                .upload_image_compressed_file_app_app_uuid_upload_image_post_with_http_info
            )
            api_ires = upload_method(
                app_uuid=self.app_id,
                image_file=upfile
            )

            spinner.stop()

            if api_ires is not None:
                status_text = " uploaded" if (api_ires.status_code == 200) else " not uploaded"
                print_feedback(f"{ipath.name}{status_text}")

        except (OSError, ApiException) as oops:
            if spinner.is_stopped is False:
                spinner.stop()
            self.logger.debug("Exception in uploading image %s", ipath)
            self.logger.debug(type(oops))
            print_text(f"Could not upload file {ipath.name}")
