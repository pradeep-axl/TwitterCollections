import json
import os


def generate_file_path(directory: str, file_name: str):
    """
    Helper function to return os independent file path
    :param directory:
    :param file_name:
    :return:
    """
    return os.path.join(os.getcwd(), directory, file_name)


def load_json_file(file_path: str):
    """
    function to load json files and read the contents
    :param file_path: str
    :return: dict
    """
    with open(file_path) as file:
        return json.loads(file.read())[0]


def load_text_file(file_path: str):
    """
    function to load input files and read the contents
    :param file_path: str
    :return:
    """
    with open(file_path) as f:
        content = f.readlines()
        return content


def get_config(key: str, path="secrets", source="twitter") -> str:
    """
    Returns the default value or the value of the environment variable.
    :param key:str name of the keys
    :param path:str represents the path to the file
    :param source: str name of the source eg. twitter, reddit.
    :return: str
    """
    # Creating os independent path to the secrete file
    path = generate_file_path(path, "secrets.json")
    # Useful when we want to provide name from environment variables for overriding values in production
    secrets = load_json_file(path)
    # TODO: Used 'source' to extend this functionality to Reedit
    if key in os.environ:
        config = os.environ[key]
    elif key in secrets[source]:
        config = secrets[source][key]
    else:
        raise OSError(f"Environment variable '{key}' is not set")
    return config


def save_json(file_name, file_content):
    """
    # Helper function to saving tweets in json files.
    :param file_content:
    :type file_name: str
    """
    with open(generate_file_path("output", file_name), 'w', encoding='utf-8') as f:
        json.dump(file_content, f, ensure_ascii=False, indent=4)