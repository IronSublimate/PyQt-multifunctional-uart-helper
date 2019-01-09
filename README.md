# PyQt5-SerialPort-Stable
PyQt5 写的智能车串口调试助手稳定版  
>作者：侯宇轩

> 本代码参考Oslomayor的PyQt5-SerialPort 
> [参考代码](https://github.com/Oslomayor/PyQt5-SerialPort-Stable)  

---

## 所用python库
1. PyQt5
2. bitarray

## 使用说明
1. 接收发送数据为普通的串口功能
2. 查看图像可以查看单片机发送的未解压图像(二值化图像，1像素占1位)，或解压后图像(灰度图像，1像素占8位)
3. 可以修改parameter.py中parameterList的参数的个数，**(同时务必修改单片机的参数的个数，使之一一对应)** 即可通过上位机改单片机的参数

## 文件说明
1. *.ui 为界面文件  
2. Ui_*.py pyuic编译.ui后的python文件  
3. CMD_Pyinstaller.bat 为 pyinstaller 打包 exe 指令  
4. ./res/icon_128.jpg 为应用程序图标  

## 开发环境
1. Python 3.6 
2. Qt Designer (用于设计界面，生成 ui 文件)
3. Visual Studio Code
4. pycharm

