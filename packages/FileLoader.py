import json

import h5py
import numpy as np
import yaml
from config.ProjectConfig import ProjectConfig
from easydict import EasyDict as edict
from yaml import FullLoader
import os


class FileLoader:
    def __init__(self) -> None:
        self.data_dir = ProjectConfig.DATA_DIR
        self.config_dir = ProjectConfig.CONFIG_DIR
        self.result_dir = ProjectConfig.RESULT_DIR


class H5pyFileLoader(FileLoader):
    def __init__(self) -> None:
        super().__init__()

    def save_h5py_file(self, file_path, file_name, dic):
        print("saving h5py file")
        f = h5py.File(file_path + file_name, 'w')
        for key in dic.keys():
            print(key, dic[key].shape)
            f.create_dataset(key, data=dic[key])
        f.close()

    def load_h5py_file(self, file_path, file_name, dic):
        print("loading h5py file")
        f = h5py.File(file_path + file_name, 'r')
        for key in dic.keys():
            dic[key] = f[key][:]
            print(key, dic[key].shape)
        f.close()
        return dic


class YamlFileLoader(FileLoader):
    def __init__(self) -> None:
        super().__init__()

    def load_yaml_file(self, file_path, file_name):
        print("loading yaml file")
        file = open(file_path + file_name, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()

        data = yaml.load(file_data)
        print(data)
        print("type：", type(data))
        return data

    def save_yaml_file(self, file_path, file_name, object):
        print("saving yaml file")
        file = open(file_path + file_name, 'w', encoding='utf-8')
        yaml.dump(object, file)
        file.close()

class NumpyFileLoader(FileLoader):
    def __init__(self) -> None:
        super().__init__()

    def load_numpy_file(self, file_path, filename):
        print("loading numpy file")
        x = np.loadtxt(file_path + '{}.txt'.format(filename), dtype=float)
        y = np.loadtxt(file_path + '{}_label.txt'.format(filename), dtype=int)
        return x, y

class JsonFileLoader(FileLoader):
    def __init__(self) -> None:
        super().__init__()

    def save_json_file(self, file_path, file_name, dict):
        print("saving json file")
        tf = open(file_path + file_name, "w")
        json.dump(dict,tf)
        tf.close()
        print("the file is located in "+ file_path + file_name)


