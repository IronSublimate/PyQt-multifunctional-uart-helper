#
# @name : 参数名
# @value : 参数值
# @paratype : 参数类型
#
import json


class Parameter:
    def __init__(self, name: str, value=0, signed=True):
        self.name = name
        self.value = value
        self.signed = signed
        # self.paratype=_paratype

    def __str__(self):
        return self.name + str(self.value) + str(self.signed)


def _fromDict(dic):
    return Parameter(dic["name"], dic["value"], dic["signed"])


parameterList = list()


def open_json():
    with open('parameter.json', 'r') as f:
        data = json.load(f)
        for d in data:
            parameterList.append(_fromDict(d))


# parameterList = [
#     Parameter("Kp", 233),
#     Parameter("Ki", 250),
#     Parameter("Kd", 12),
# ]

if __name__ == '__main__':
    open_json()
    for i in parameterList:
        print(str(i))
