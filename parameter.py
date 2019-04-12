#
# @name : 参数名
# @value : 参数值
# @paratype : 参数类型
#
import json


# class Parameter:
#     def __init__(self, name: str, pos: str, value: str):
#         self.name = name
#         self.value = value
#         self.pos = pos
#         # self.signed = signed
#         # self.paratype=_paratype
#
#     def __str__(self):
#         return self.name + str(self.value) + str(self.pos)


# def _fromDict(dic):
#     return Parameter(dic["name"], dic["value"], dic["signed"])
#
#
# parameterList = list()
#
#
# def open_json():
#     with open('parameter.json', 'r') as f:
#         data = json.load(f)
#         for d in data:
#             parameterList.append(_fromDict(d))
#
#
# # parameterList = [
# #     Parameter("Kp", 233),
# #     Parameter("Ki", 250),
# #     Parameter("Kd", 12),
# # ]
#
# if __name__ == '__main__':
#     open_json()
#     for i in parameterList:
#         print(str(i))
