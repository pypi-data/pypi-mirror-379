""" Module for Asymmetric Cryptography """
import yaml
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
# Deprecated backend selection
# from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# - PGPy does not support python >= 3.13
#   because module is imghdr is not builtin anymore
# from pgpy import PGPKey, PGPMessage

from celestical.config.config import Config
from celestical import api

class Cryptic:
    """
    A class used for Encrpyting client documents
    """
    def __init__(self,
                 public_key: str = "",
                 config: Config = None
                 ):
        """ Initializing the cryptic object with the given public key
        or get it from the API (default)

        """
        self.config = config
        if config is None:
            self.config = Config()

        self.public_key = None

        # Retrieve the public key from the API
        if public_key == "":
            try:
                apiconf = self.config.api_configuration()
                with api.ApiClient(apiconf) as api_client:
                    utils = api.UtilsApi(api_client)
                    api_response = utils.\
                            pubkey_u_public_key_get()
                    public_key = api_response.public_key

                public_key = public_key.encode(self.config.encoding)
            except (api.ApiException, OSError, ValueError) as oops:
                msg = "encryption: failed to fetch the public key"
                self.config.logger.critical(msg)
                self.config.logger.critical(oops)

            try:
                # Serializing the public key
                self.public_key = serialization.load_pem_public_key(
                    public_key,
                    # --- Backend has been deprecated
                    # backend=default_backend()
                    )
            except (ValueError, TypeError, OSError) as oops:
                msg = "encryption: failed to serialize the public key"
                self.config.logger.critical(msg)
                self.config.logger.critical(oops)
                self.public_key = None

    def encryption(self,
                   data: dict,
                   ) -> bytes | None:
        """ Encryption of the data from the data given

        Arguments:
            - data: a dictionary to be fully encrypted

        Returns:
            - encrypted_data: as bytes
        """
        if self.public_key is None:
            # We cannot encrypt yet. The pub key is not set.
            return None

        # Turn the dictionary data into yaml str then UTF-8 bytes
        data = yaml.safe_dump(data, default_flow_style=False
            ).encode(self.config.encoding)

        try:
            encrypted_data = self.public_key.encrypt(
                            data,
                            padding.OAEP(
                                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                algorithm=hashes.SHA256(),
                                label=None
                            ))
        except (ValueError, TypeError, OSError) as oops:
            msg = f"encryption: failed to encrypt the data as {oops}"
            self.config.logger.critical(msg)
            encrypted_data = ""
            return encrypted_data

        return encrypted_data

    def is_ready(self) -> bool:
        """Check if the encryption is ready to use.
        
        Returns:
            bool: True if public key is loaded, False otherwise
        """
        return self.public_key is not None
