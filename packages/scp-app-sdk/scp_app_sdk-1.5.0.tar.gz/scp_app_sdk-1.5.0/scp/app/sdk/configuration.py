import json
import sys
import os

def get_inputs():
    """
    Get the provided cnfiguration as a Python object
    ( ie like json.load(sys.stdin) )

    :return: A python object representing the application configuration
    """
    return json.load(sys.stdin)

def get_user_id():
    """
    Get User ID

    :return: A string contaning the User ID
    """
    return os.environ.get("USER_ID", None)

def get_migrate_versions():
    """
    Get version information during up/down-grading of an application.

    :return: A dictionary containing from_build_version and to_build_version
    """
    return {key.lower(): value for key, value in dict(os.environ).items() if key in ["FROM_BUILD_VERSION", "TO_BUILD_VERSION"]}
