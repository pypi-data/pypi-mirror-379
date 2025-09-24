import getpass
import subprocess

from cachetools import cached, TTLCache

from mst.core.usage_logger import LogAPIUsage


class AuthSRV:
    """Interface for AuthSRV credential retrieval."""

    def __init__(self, path: str = ""):
        """Create instance of AuthSRV, optionally setting prefix for authsrv executeables,
        should end in platform specific path separator.

        Args:
            path (str, optional): Prefix for authsrv executeables,
                should end in platform specific path separator. Defaults to "".
        """
        self.authsrv_decrypt = f"{path}authsrv-decrypt"
        self.authsrv_raw_encrypt = f"{path}authsrv-raw-encrypt"

    def fetch(self, instance: str, owner=None, user=None):
        """returns stashed password, "user" defaults to the current userid on unix.
        If running as root, "owner" can be specified.

        Args:
            owner (str): If running as root, "owner" can be specified. Defaults to getpass.getuser().
            user (str): Defaults to the current user.
            instance (str): instance name.

        Raises:
            ValueError: When instance is not defined

        Returns:
            str: the fetched value from authsrv-decrypt
        """
        LogAPIUsage()

        current_user = getpass.getuser()

        if not owner:
            owner = current_user
        elif owner != current_user and current_user != "root":
            owner = current_user

        if not user:
            user = current_user

        if instance is None:
            raise ValueError(__name__, "(): instance must be defined")

        return _fetch(self.authsrv_decrypt, owner, user, instance)

    def store(self, password: str, instance: str, owner: str = None, user: str = None):
        """
        Store the given instance/password in authsrv backend.
        """
        current_user = getpass.getuser()

        if not owner:
            owner = current_user
        elif owner != current_user and current_user != "root":
            owner = current_user

        if not user:
            user = current_user

        if instance is None:
            raise ValueError(__name__, "(): instance must be defined")

        # store secret
        subprocess.run(
            [self.authsrv_raw_encrypt, owner, user, instance],
            input=password,
            encoding="utf_8",
            check=True,
        )

        # nb. always clear cache to avoid stale entries
        self.clear_cache()

    def clear_cache(self):
        """
        Clear cache of fetched credentials.
        """
        _fetch.cache_clear()


@cached(TTLCache(maxsize=20, ttl=60))
def _fetch(authsrv_decrypt, owner, user, instance):
    """
    Logic to fetch credentials from authsrv; this is kept outside of
    the class because we need the cache to span multiple authsrv
    instances.
    """
    return subprocess.check_output([authsrv_decrypt, owner, user, instance]).decode("utf-8").rstrip("\r\n")
