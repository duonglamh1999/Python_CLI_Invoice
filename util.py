import os
from configparser import ConfigParser



def is_file(path:str):
    return os.path.isfile(path)


def read_config(field: str):
    config_object = ConfigParser()
    config_object.read("config.ini")
    return config_object["INFO"][field]


def get_year():
    return int(input('year?'))


def get_month():
    month= int(input('month?'))
    if month >12 or month <1:
        raise Exception("Invalid Month")
    else:
        return month

def get_path (year:int,month:int):
    root_path = read_config("root_path")
    return rf'{root_path}{year}-{month}-invoice'


