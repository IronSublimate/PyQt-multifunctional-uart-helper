#
# @name : 参数名
# @value : 参数值
# @paratype : 参数类型
#
class Parameter:
    def __init__(self, _name: str, _value=0, _signed=True):
        self.name = _name
        self.value = _value
        self.signed = _signed
        # self.paratype=_paratype


parameterList = [
    Parameter("Kp", 233),
    Parameter("Ki", 250),
    Parameter("Kd", 12),
]
