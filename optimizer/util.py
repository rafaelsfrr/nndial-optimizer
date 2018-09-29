import configparser
import shutil
import os
import argparse


def load_config_file(path, section):
    """
    :param path: the path of the config file to be loaded
    :param section: the section of the config file that should be loaded
    :return: the value of the config file section
    """

    config = configparser.ConfigParser()
    config.read(path)
    return [config[section][key] for key in config[section]]


def write_config_file(list, path):
    """
    :param list: the list with arguments to be write
    :param path:  the path to save the file
    :return: none
    """

    config = configparser.ConfigParser()

    config.read('config/NDM.cfg')
    config['learn']['lr'] = str(round(list[0], 3))
    config['learn']['lr_decay'] = str(round(list[1], 2))
    config['learn']['l2'] = str(round(list[2], 5))
    config['learn']['random_seed'] = str(int(list[3]))

    with open(path, 'w') as configfile:
        config.write(configfile)


def move_file(file_init, file_final):
    """
    :param file_init: the path to the file to be copied
    :param file_final: the path to save the copied file
    :return: none
    """
    shutil.copyfile(file_init, file_final)


def remove_file(path):
    """
    :param path: the of the file to be removed
    :return: none
    """
    os.remove(path)


def make_args(config, mode):
    """
    :param config: the config file
    :param mode: the mode
    :return: the args namespace
    """

    return argparse.Namespace(config=config, mode=mode)


def format_args(args):
    """
    :param args: the args to be formated
    :return: the args formated
    """

    args_formated = list()
    args_formated.append(round(args[0], 3))
    args_formated.append(round(args[1], 2))
    args_formated.append(round(args[2], 5))
    args_formated.append(int(args[3]))

    return args_formated
