import ejson
import configparser
class ConfigError(BaseException):
    def __init__(self,text):
        pass
class Config:
    def __init__(self,file,type="json"):
        self.type = type
        self.file = file
        if type == "json":
            self.config = ejson.Json(self.file)
        else:
            raise ConfigError("Can`t read a TYPE attribute")