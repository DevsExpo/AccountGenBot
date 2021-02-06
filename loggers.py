import os
import sys
from distutils.util import strtobool as sb
from logging import DEBUG, INFO, basicConfig, getLogger
from distutils.util import strtobool as sb
from logging import DEBUG, WARNING, basicConfig, getLogger, INFO
from logging.handlers import RotatingFileHandler
from pathlib import Path
from sys import argv
from telethon import TelegramClient, events, functions, types
import asyncio
import glob
import logging
import sys
from pathlib import Path
import telethon.utils
from telethon import TelegramClient

ENV = os.environ.get("ENV", False)
if ENV:
    from Configs import Config
else:
    from local_config import Development as Config

ENV = os.environ.get("ENV", False)
if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=INFO
        )
    logger = getLogger(__name__)
