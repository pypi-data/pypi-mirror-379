"""Sync IAM users and identities into Rucio accounts."""

import logging
import os
import time
from configparser import ConfigParser
from typing import Optional

import requests
from rucio.client.accountclient import AccountClient
from rucio.common.exception import AccountNotFound, RucioException

logging.basicConfig(level=logging.INFO)

CONFIG_ENV_VAR = "BDMS_SYNC_CONFIG"


class IAMRucioSync:
    """Synchronize IAM accounts, identities into Rucio."""

    TOKEN_URL = "/token"

    def __init__(self, config_path: str):
        """Initialize the syncer and load configuration."""
        self.config_path = config_path
        self.iam_server = None
        self.client_id = None
        self.client_secret = None
        self.max_retries = 5
        self.delay = 10  # seconds
        self.account_client = AccountClient()
        self.configure()

    def configure(self) -> None:
        """Load configuration from file and environment variables."""
        cfg = ConfigParser()
        cfg.read(self.config_path)
        self.iam_server = cfg.get("IAM", "iam-server")
        self.client_id = cfg.get("IAM", "client-id")
        self.client_secret = cfg.get("IAM", "client-secret")
        self.max_retries = int(
            cfg.getint("IAM", "max-retries", fallback=self.max_retries)
        )
        self.delay = float(cfg.getint("IAM", "delay", fallback=self.delay))
        if not all([self.iam_server, self.client_id, self.client_secret]):
            raise ValueError("Incomplete IAM config")

    def get_token(self) -> str:
        """Obtain an access token from the IAM server."""
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": "scim:read",
        }
        logging.info(
            "Requesting IAM token from %s using the client_id %s",
            self.iam_server + self.TOKEN_URL,
            self.client_id,
        )
        for attempt in range(1, self.max_retries + 1):
            try:
                r = requests.post(
                    self.iam_server + self.TOKEN_URL,
                    data=data,
                    timeout=30,
                )
                r.raise_for_status()  # exception is status!=200
                js = r.json()
                if "access_token" not in js:
                    raise RuntimeError(f"No access_token in response: {js}")
                return js["access_token"]

            except (requests.RequestException, RuntimeError) as e:
                if attempt < self.max_retries:
                    logging.error(
                        "attempt %d failed: %s. Retrying in %d seconds...",
                        attempt,
                        e,
                        self.delay,
                    )
                    time.sleep(attempt * self.delay)
                else:
                    raise

    def get_users(self, token: str) -> list[dict]:
        """Fetch users from IAM using SCIM API."""
        start = 1
        count = 100
        headers = {"Authorization": f"Bearer {token}"}
        users = []
        processed = 0
        while True:
            params = {"startIndex": start, "count": count}
            r = requests.get(
                f"{self.iam_server}/scim/Users",
                headers=headers,
                params=params,
                timeout=30,
            )
            data = r.json()
            users.extend(data.get("Resources", []))
            processed += data.get("itemsPerPage", 0)
            if processed < data.get("totalResults", 0):
                start += count
            else:
                break
        logging.info("Fetched %d IAM users", len(users))
        return users

    def ensure_group_account(self, account_name: str) -> bool:
        """Ensure a Rucio account exists for the given user."""
        try:
            self.account_client.get_account(account_name)
            return False
        except AccountNotFound:
            self.account_client.add_account(account_name, "GROUP", email="")
            return True

    def existing_identities(self, account: str) -> set[str]:
        """Return the existing identities for a given account."""
        try:
            return {i["identity"] for i in self.account_client.list_identities(account)}
        except RucioException as e:
            logging.error("List identities failed %s: %s", account, e)
            return set()

    def sync_x509(self, users: list[dict]) -> None:
        """Sync IAM X.509 certificates into Rucio identities."""
        for user in users:
            email = self._get_user_email(user)
            for group in user.get("groups", []):
                groupname = group.get("display")
                self.ensure_group_account(groupname)
                certificates = self._get_user_certificates(user)
                self._sync_group_certificates(groupname, email, certificates)

    def _get_user_email(self, user: dict) -> str:
        return user.get("emails", [{}])[0].get("value", "")

    def _get_user_certificates(self, user: dict) -> list[dict]:
        indigo = user.get("urn:indigo-dc:scim:schemas:IndigoUser", {})
        return indigo.get("certificates", [])

    def _sync_group_certificates(
        self, groupname: str, email: str, certificates: list[dict]
    ) -> None:
        existing_identities = self.existing_identities(groupname)
        for cert in certificates:
            dn = self._extract_dn(cert)
            if not dn:
                continue
            if dn in existing_identities:
                logging.info("Identity %s already exists for group %s", dn, groupname)
                continue
            self._add_x509_identity(dn, groupname, email)

    def _extract_dn(self, cert: dict) -> Optional[str]:
        dn = cert.get("subjectDn")
        if not dn:
            logging.error("Missing subjectDn in %s", cert)
            return None
        return self.to_gridmap(dn)

    def _add_x509_identity(self, dn: str, groupname: str, email: str) -> None:
        try:
            self.account_client.add_identity(
                identity=dn,
                authtype="X509",
                account=groupname,
                email=email,
                default=True,
            )
            logging.info("Added X509 identity %s for group %s", dn, groupname)
        except Exception as e:
            logging.error("X509 add failed %s: %s", groupname, e)

    @staticmethod
    def to_gridmap(dn: str) -> str:
        """Convert a DN string into gridmap format."""
        parts = dn.split(",")
        parts.reverse()
        return "/".join(parts)


def main():
    """Entry point: run the IAM → Rucio synchronization."""
    config_path = os.environ.get(CONFIG_ENV_VAR)
    if not config_path:
        raise SystemExit(
            "Config path required. Use --config or set %s.", CONFIG_ENV_VAR
        )
    if not os.path.isfile(config_path):
        raise SystemExit(f"Config file not found: {config_path}")

    syncer = IAMRucioSync(config_path)
    token = syncer.get_token()
    users = syncer.get_users(token)
    syncer.sync_x509(users)
    logging.info("Sync done.")


if __name__ == "__main__":
    main()
