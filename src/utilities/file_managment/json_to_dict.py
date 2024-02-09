import json
import logging

ModuleLogger = logging.getLogger(__name__)


def get_dict(file: str) -> dict:
    """Makes dictionary from json file.

    :param file: str, file path.
    :returns: python dictionary,
    :rtype: dict.
    """
    try:
        with open(file, "r") as file:
            return json.load(file)

    except(FileNotFoundError, FileExistsError) as E:
        ModuleLogger.error(msg=f"{file} raised error:{E}")
