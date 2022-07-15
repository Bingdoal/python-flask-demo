import yaml


class Config:
    def __init__(self, profile="default", path="config/"):
        self.__profile = profile
        self.__path = path
        self.__docs = []
        self.__load_config()

    def __load_config(self):
        file_name = "config.yaml"
        stream = open(self.__path + file_name, "r")
        docs = yaml.load(stream, yaml.FullLoader)
        self.__docs = docs

        if self.__profile != "default":
            file_name = "config." + self.__profile + ".yaml"
            stream = open(self.__path + file_name, "r")
            docs = yaml.load(stream, yaml.FullLoader)
            self.__replace_dict(self.__docs, docs)

        print(self.__docs)

    def __replace_dict(self, source, target):
        for k, v in target.items():
            if k in source and type(source[k]) is dict and type(v) is dict:
                self.__replace_dict(source[k], v)
            elif source[k] is not dict and v is not dict:
                source[k] = v

    def get(self, path: str):
        paths = path.split(".")
        position = self.__docs
        for p in paths:
            if type(position) is dict:
                position = position[p]
            else:
                return None

        return position

    def get_str(self, path: str):
        return str(self.get(path))
