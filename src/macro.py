import json


def read_macro():
    try:
        f = open('../macro.json', 'r')
    except FileNotFoundError:
        # QMessageBox.warning(self, '警告', '在当前目录下未找到setting.json')
        return None
    else:
        try:
            data = json.load(f)
            return data
        finally:
            f.close()


if __name__ == '__main__':
    dic = read_macro()
    l=dic["stop"]
