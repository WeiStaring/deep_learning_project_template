from utils.FileLoader import YamlFileLoader

yaml_loader = YamlFileLoader()
a = {"a": 1,"b":1}
yaml_loader.save_yaml_file("config.yaml", a)
