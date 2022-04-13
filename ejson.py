import json
class Json:
    def __init__(self,path,mode="r"):
        if mode == "r":
            file = open(path, "r")
            js = file.read()
            file.close()
            js = json.loads(js)
            self._obj = js
            self._path = path
        if mode == "w":
            self.file = open(path, "w")
            self._obj = ""
    def update(self):
        temp = Json(self._path,"w")
        temp.write(json.dumps(self._obj,indent=4))
        temp.close()
    def write(self,content):
        self.file.write(str(content).replace("'",'"'))
    def close(self):
        self.file.close()
    def __getitem__(self,item):
        return self._obj[item]
    def __setitem__(self, key, value):
        self._obj[key] = value
    def __str__(self):
        return str(self._obj)
    def __repr__(self):
        return str(self._obj)
    def __eq__(self,other):
        return self._obj == other._obj
