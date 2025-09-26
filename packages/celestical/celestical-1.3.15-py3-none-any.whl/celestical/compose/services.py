"""
This module contains classes related to prepare command of celestical CLI tool
"""
from pathlib import Path
from typing import Tuple
import typer
from celestical.config import Config
from celestical.utils.prompts import prompt_metadata_base_domain
from celestical.utils.display import (
    print_feedback,
    cli_panel,)
from celestical.utils.prompts import (
    prompt_user,
    confirm_user)
from celestical.compose.compose import Compose


class Enricher:
    """
    This class consist of attributes and methods to prepare the ecompose file
    """

    SERVICE_TYPES = {
        "FRONTEND": ["web", "www", "frontend", "traefik", "haproxy",
                     "apache", "nginx"],
        "API": ["api", "backend", "service", "node"],
        "DB": ["database", "redis", "mongo", "mariadb", "postgre"],
        "BATCH": ["process", "hidden", "compute"],
        "OTHER": []
        }

    def __init__(self,
            compose:Compose,
            config:Config = None,
            ) -> None:
        """ The Enricher will work on an injected e-compose file
        """
        self.compose = compose
        self.config = config
        if self.config is None:
            self.config = Config()

    def richformat_services(self, services:dict) -> str:
        """ Create a rich formatted string to display a bullet list for
        services
        """
        s_info = ""
        for serv in services:
            image = services[serv].get("image", "-undefined-")
            s_info += f"\t- [yellow]{serv}[/yellow] (image)--> {image}\n"
        return s_info

    def guess_service_type_by_name(self, service_name: str, img_name:str=""):
        """ Quick guess of service type
        """

        if len(service_name) == 0:
            return ""

        service_name = service_name.lower()

        for stype in self.SERVICE_TYPES:
            for guesser in self.SERVICE_TYPES[stype]:
                if guesser in service_name:
                    return stype

        if img_name != "":
            img_name = img_name.lower()
            for stype in self.SERVICE_TYPES:
                for guesser in self.SERVICE_TYPES[stype]:
                    if guesser in img_name:
                        return stype

        # if nothing found
        return "OTHER"

    def confirm_enrichment(
            self,
            ecompose_path: Path,
            selected_path: Path,
            ) -> Tuple[Path, dict, dict]:
        """ Find the compose file in the given folder if it is a folder and
        decide where the enriched compose file will be. Check with the user if
        enrichment is necessary when already present.

        Arguments:
          - ecompose_path: ecompose file path
          - selected_path: path of the selected c_dist compose file

        Returns: three elements:
          - boolean if enrichment is confirmed
          - (deprecated) 'ecomp_path' the path to the found most recent
            docker-compose or enriched file
            --> becomes the ecompose path of the App object.
          - (deprecated) c_dict: the python dictionary of that most recent
            compose file content with first metadata containing info if user
            wants to enrich or not. From confirmation ask thanks to timestamp
            comparison.
            --> c_dict is or become the ecompose here. no need to return it.
          - (deprecated) prev_dict: the python dictionary of the enriched file anyway
            found, so it can be used for default values while enriching to
            fasten and ease the process. Would be the ecompose_path anyhow.
            --> temporary initial ecompose content, can be found in disk.
        """
        # --- Loading compose and ecompose files
        prev_dict = self.compose.read_docker_compose(ecompose_path)
        self.compose.safe_update(prev_dict)

        c_dict = {}
        if ecompose_path == selected_path:
            # We are working on ecompose only
            c_dict = prev_dict.copy()
        else:
            # We are working on user define compose
            c_dict = self.compose.read_docker_compose(selected_path)


        # --- processing selected compose file
        if c_dict != {}:
            # - loading potential environment variables and files
            c_dict = self.compose.integrate_all_env(c_dict,
                                                    selected_path.parent)

            # - make generated image name for images built in the compose file
            c_dict = self.compose.use_built_image_names(c_dict, selected_path)

            # Add all the information to ecompose dictionary
            self.compose.update(c_dict)

            s_info = "\n* [underline]Selected App domain[/underline]: " \
                    +"[blue]" \
                    +f"{self.compose.get('base_domain')}" \
                    +"[/blue]\n"

            s_info += "\n* [underline]File[/underline] of your orchestration:\n"
            s_info += f"\t[green]{selected_path}[/green]\n"

            s_info += "\n* [underline]Services[/underline] found: \n"
            s_info += self.richformat_services(self.compose.services)

            # - show users a recap of services in pointed compose dict
            cli_panel(s_info, title="Quick review of your App")

            # - case where we are already on enriched content
            # Test differently apart from celestical (celestical type)
            is_cel_type = True
            for serv in self.compose.services:
                if "celestical_type" not in serv:
                    is_cel_type = False
                    break

            if is_cel_type is True:
                msg = "(Yes) To deploy now | (No) To reset info"
                answer = confirm_user(msg, default=True)

                if answer:
                    # Skip enrichment
                    self.compose.set("skip_enrich", True)
                    return False
                # else will lead to enrichment (reset)
                self.compose.set("skip_enrich", False)
                return True

            # - case where we are on an user compose file
            answer = confirm_user("Continue with this file", default=True)

            if answer:
                self.compose.set("skip_enrich", False)
                return True

            # - case where we exit for another file
            cli_panel("Give another path on command line: \n"
                    +"\t=> celestical deploy /path/to/another-compose.yml")
            raise typer.Abort()

        cli_panel("No docker compose content was found at:\n"
                +f"{selected_path}\n\n"
                +"Give another docker-compose path on command line: \n"
                +"\t=> [yellow]celestical deploy "
                +"/path/to/docker-compose.yml[/yellow]")
        self.config.logger.debug("exiting as no docker compose file found")
        raise typer.Abort()

    def enrich_compose(
            self,
            prev_comp:dict = {}) -> dict:
        """ Enrich a stack with additional information about the services.

        Arguments:
          - prev_comp(dict): often the previous ecompose file
            for default values
        Returns:
            (dict): enriched docker-compose.yml file content
        """
        # enriched_compose: dict = self.compose.ecompose

        # extracting default values that could be set here
        def_app_name: str = self.compose.get("name")
        def_base_domain: str = self.compose.get("base_domain")

        # --- metadata: base domain
        # only ask when the base_domain is not already defined
        # or too short defined. "a.c"
        if def_base_domain is None or len(def_base_domain) < 3:
            self.compose.init_ecompose()

        # --- summarizing current services in docker compose file
        services = self.compose.services
        msg = "[underline]Here is a quick recap[/underline]\n\n"
        msg += "Your App: [green]"
        msg += f"{self.compose.get('name')}[/green]\n"
        msg += "Website: [green]https://"
        msg += f"{self.compose.get('base_domain')}[/green]\n"
        msg += "runs the following services:\n"
        msg += self.richformat_services(services)
        msg += "\n\n[yellow]We will tag services by usage tag[/yellow]:\n"

        serveme_types = [serv for serv in self.SERVICE_TYPES]

        help_on_types = "Type the type number or name\n"
        for n in range(len(serveme_types)):
            help_on_types += f"\t{n+1} --> {serveme_types[n]}\n"

        cli_panel(msg+help_on_types)

        counter: int = 1
        for service_name in services:
            # --- display current service name and guessed type
            msg = f"Choose a type for service #{counter} of {len(services)}: "
            msg += f"[yellow]{service_name}[/yellow] --> "

            img_name = services[service_name].get("image", "")
            stype = self.guess_service_type_by_name(service_name, img_name)
            msg += f" detected type: [purple]{stype}[/purple]"

            # --- ask for a better categorization
            prompt_done = False
            while prompt_done is False:
                type_nbr:str = prompt_user(
                    msg,
                    default=stype,
                    helptxt=help_on_types)
                type_nbr = type_nbr.strip()
                type_nbr = type_nbr.upper()
                serveme_types = list(self.SERVICE_TYPES)
                prompt_done = True
                match type_nbr:
                    case "1":
                        stype = serveme_types[0]
                    case "2":
                        stype = serveme_types[1]
                    case "3":
                        stype = serveme_types[2]
                    case "4":
                        stype = serveme_types[3]
                    case "5":
                        stype = serveme_types[4]
                    case _:
                        # type_nbr might be something else
                        if type_nbr == "":
                            #stype is already set
                            prompt_done = True
                        elif type_nbr in self.SERVICE_TYPES:
                            stype = type_nbr
                            prompt_done = True
                        else:
                            prompt_done = False

            self.compose.set_semantics(service_name, stype)

            print_feedback(self.compose.get_semantics(service_name))

            msg = "[underline]Public URL[/underline] for service "
            msg += f"[yellow]{service_name}[/yellow] "
            service_url: str = prompt_user(
                msg,
                default="",
                helptxt="Leave empty if none")

            if service_url != "":
                self.compose.ecompose["services"][
                    service_name]["celestical_url"] = service_url
                print_feedback(
                    self.compose.ecompose["services"][
                        service_name]["celestical_url"])

            # TODO get image hash or not
            # enriched_compose["services"][
            #  service_name]["celestical_image_hash"] = service_name["image"]
            counter += 1

        return self.compose.ecompose

    def prepare(
            self,
            ecompose_path: Path,
            selected_path: Path,
        ) -> Compose:
        """
        This function prepares the enriched compose file and saves it.
        - compose_path:str: path to the docker compose file
        """
        # --- Find file and verify path and previous enrichment
        do_enrich:bool = self.confirm_enrichment(
            ecompose_path=ecompose_path,
            selected_path=selected_path)

        # --- Get info from user to enrich context
        enriched_compose = {}
        if do_enrich:
            self.compose.ecompose = self.enrich_compose()
                # (comp_dict, prev_comp, ecomp_path)

            # we reread the compose so that we can audit what is posted
            # enriched_compose = self.compose.read_docker_compose(enriched_compose_path)

        self.compose.integrate_top_secrets(selected_path.parent)

        # --- save the enriched content
        return self.compose
