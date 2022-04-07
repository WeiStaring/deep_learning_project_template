import h5py
import numpy as np
import yaml
import os


class FileLoader:
    def __init__(self) -> None:
        self.data_dir = 'data/'
        self.setting_dir = 'config/'


class H5pyFileLoader(FileLoader):
    def __init__(self) -> None:
        super().__init__()

    def save_h5py_file(self, file_name, dic):
        print("saving h5py file")
        f = h5py.File(self.data_dir + file_name, 'w')
        for key in dic.keys():
            print(key, dic[key].shape)
            f.create_dataset(key, data=dic[key])
        f.close()

    def load_h5py_file(self, file_name, dic):
        print("loading h5py file")
        f = h5py.File(self.data_dir + file_name, 'r')
        for key in dic.keys():
            dic[key] = f[key][:]
            print(key, dic[key].shape)
        f.close()
        return dic


class YamlFileLoader(FileLoader):
    def __init__(self) -> None:
        super().__init__()

    def load_yaml_file(self, file_name):
        print("loading yaml file")
        file = open(self.setting_dir + file_name, 'r', encoding="utf-8")
        file_data = file.read()
        file.close()

        data = yaml.load(file_data)
        print(data)
        print("类型：", type(data))
        return data

    def save_yaml_file(self, file_name, object):
        print("saving yaml file")
        file = open(self.setting_dir + file_name, 'w', encoding='utf-8')
        yaml.dump(object, file)
        file.close()


class NumpyFileLoader(FileLoader):
    def __init__(self) -> None:
        super().__init__()

    def load_numpy_file(self, filename):
        print("loading numpy file")
        x = np.loadtxt(self.data_dir + '{}.txt'.format(filename), dtype=float)
        y = np.loadtxt(self.data_dir + '{}_label.txt'.format(filename), dtype=int)
        return x, y
