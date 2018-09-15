import configparser
import shutil


def load_config_file(path):
    """
    :param path: the path of the config file to be loaded
    :return: the config file
    """

    config = configparser.ConfigParser()
    return config.read(path)


def write_config_file(config, path):
    """
    :param config: the config file
    :param path:  the path to save the file
    :return: none
    """

    with open(path, 'w') as configfile:
        config.write(configfile)


def move_file(file_init, file_final):
    """
    :param file_init: the path to the file to be copied
    :param file_final: the path to save the copied file
    :return: none
    """
    shutil.copyfile(file_init, file_final)
