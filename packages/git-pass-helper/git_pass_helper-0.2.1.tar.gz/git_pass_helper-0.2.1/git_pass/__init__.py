import argparse
import dotenv
import tempfile
import subprocess
import os

from urllib.parse import urlparse


def main() -> None:
    dotenv.load_dotenv()

    default_username = os.environ.get("GIT_PASS_USER", "user")
    default_password = os.environ.get("GIT_PASS_PASSWORD", None)
    default_url = os.environ.get("GIT_PASS_URL", "https://github.com")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--username", default=default_username, help="The username for basic auth"
    )
    parser.add_argument(
        "-p", "--password", default=default_password, help="The password for basic auth"
    )
    parser.add_argument(
        "-U",
        "--url",
        default=default_url,
        help="The prefix url to use the credentials for",
    )
    parser.add_argument("cmd", metavar="CMD", nargs="*", help="The command to execute")
    args = parser.parse_args()

    if args.password is None:
        parser.error("Please supply a password")

    url = urlparse(args.url)

    cmd = [os.environ.get("SHELL", "/bin/sh")] if len(args.cmd) == 0 else args.cmd

    path: str | None = None
    try:
        fd, path = tempfile.mkstemp(suffix=".tmp", prefix="git_pass_")
        with os.fdopen(fd, "w") as tmp:
            auth = f"{args.username}:{args.password}"
            tmp.write(f"{url.scheme}://{auth}@{url.hostname}{url.path}\n")

        cnt = int(os.environ.get("GIT_CONFIG_COUNT", 0)) + 1
        os.environ["GIT_CONFIG_COUNT"] = str(cnt)
        os.environ[f"GIT_CONFIG_KEY_{cnt-1}"] = f"credential.{args.url}.helper"
        os.environ[f"GIT_CONFIG_VALUE_{cnt-1}"] = f"store --file {path}"

        rc = subprocess.run(cmd)
    finally:
        if path is not None:
            os.remove(path)

    exit(rc.returncode)


if __name__ == "__main__":
    main()
