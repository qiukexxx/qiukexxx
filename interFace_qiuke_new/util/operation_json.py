# coding=utf-8
# 封装对json文件的操作
import json

class operationJson:
    """操作json文件"""

    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = "../data/data.json"
        else:
            self.file_path = file_path

    def read_data(self):
        """读取json文件"""
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        """根据关键字获取对应数据"""
        self.data = self.read_data()
        return self.data[id]

    def write_data(self,data):
        """写入内容到json"""
        with open(self.file_path,'w') as fp:
            fp.write(json.dumps(data))

    def write_data_with_key_and_velue(self,key,velue):
        """以键值对的方式写入json"""
        jsondata = self.read_data()
        jsondata[key] = velue
        with open(self.file_path,"w") as fp:
            fp.write(json.dumps(jsondata))


if __name__ == "__main__":
    url = operationJson(file_path='../data/url.json').get_data('url')
    print(url)
    data = {"wanggeToken":"iiwowowkssjsjs"}
    operationJson(file_path='../data/token.json').write_data_with_key_and_velue("shequToken","9980000")
