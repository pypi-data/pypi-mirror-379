"""Change portfolio password."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import override

from colorama import Fore

from nummus.commands.base import BaseCommand


class ChangePassword(BaseCommand):
    """Change portfolio password."""

    NAME = "change-password"
    HELP = "change portfolio password"
    DESCRIPTION = "Change database and/or web password"

    def __init__(
        self,
        path_db: Path,
        path_password: Path | None,
        path_password_new: Path | None,
    ) -> None:
        """Initialize create command.

        Args:
            path_db: Path to Portfolio DB
            path_password: Path to password file, None will prompt when necessary
            path_password_new: Path to new password file,
                None will prompt when necessary

        """
        super().__init__(path_db, path_password)
        self._path_password_new = path_password_new

    @override
    @classmethod
    def setup_args(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            "--new-pass-file",
            dest="path_password_new",
            metavar="PATH",
            type=Path,
            help=argparse.SUPPRESS,
        )

    @override
    def run(self) -> int:
        # Defer for faster time to main
        from nummus import portfolio

        p = self._p

        new_db_key, new_web_key = self._get_keys()
        if new_db_key is None and new_web_key is None:
            print(f"{Fore.YELLOW}Neither password changing", file=sys.stderr)
            return -1

        # Back up Portfolio
        _, tar_ver = p.backup()
        try:
            if new_db_key is not None:
                p.change_key(new_db_key)

            if new_web_key is not None:
                p.change_web_key(new_web_key)
        except Exception:  # pragma: no cover
            # No immediate exception thrown, can't easily test
            portfolio.Portfolio.restore(p, tar_ver=tar_ver)
            print(f"{Fore.RED}Abandoned password change, restored from backup")
            raise
        print(f"{Fore.GREEN}Changed password(s)")
        print(f"{Fore.CYAN}Run 'nummus clean' to remove backups with old password")
        return 0

    def _get_keys(self) -> tuple[str | None, str | None]:
        if self._path_password_new:
            with self._path_password_new.open("r", encoding="utf-8") as file:
                new_db_key = file.readline().split(":", 1)[-1].strip() or None
                new_web_key = file.readline().split(":", 1)[-1].strip() or None
            return new_db_key, new_web_key

        from nummus import utils

        new_db_key: str | None = None
        new_web_key: str | None = None
        if utils.confirm("Change portfolio password?"):
            new_db_key = utils.get_password()
            if new_db_key is None:
                # Canceled
                return None, None

        if (self._p.is_encrypted or new_db_key is not None) and utils.confirm(
            "Change web password?",
        ):
            new_web_key = utils.get_password()
            if new_web_key is None:
                # Canceled
                return None, None

        return new_db_key, new_web_key
