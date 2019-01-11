# PyQt5-SerialPort-Stable
#### PyQt5 智能车串口调试助手稳定版  

--- 
>作者：侯宇轩  
> 本代码参考Oslomayor的PyQt5-SerialPort 
> [参考代码](https://github.com/Oslomayor/PyQt5-SerialPort-Stable)  
---

## 所用python库
1. PyQt5

## 使用说明
1. 接收发送数据为普通的串口功能
2. 查看图像可以查看单片机发送的未解压图像(二值化图像，1像素占1位)，
或解压后图像(灰度图像，1像素占8位)，使用键盘P键暂停，
点击保存图像按钮将图像保存在./output目录下
3. 可以修改parameter.json中parameterList的参数的个数，
**(同时务必修改单片机的参数的个数，使之一一对应)** 即可通过上位机改单片机的参数
4. 打开程序时最好在程序同级目录下有parameter.json文件

## 数据传输格式
#### 调参模式
上位机更新单片机：  
hyxw\[数据号(0-255)\]\[数据值int32(小端模式)\]  
e.g. hyxw12300  
上位机更新单片机：  
上位机发送 hyxr  
上位机接收   
for item in list:  
&nbsp;&nbsp;&nbsp;&nbsp;item.value=\[数据值int32(小端模式)\]  

#### 图像模式
单片机发送图像前必须先发送0x01 0xfe，表示图像的开始

## 文件说明
1. *.ui 为界面文件  
2. Ui_*.py pyuic编译.ui后的python文件  
3. CMD_Pyinstaller.bat 为 pyinstaller 打包 exe 指令  
4. ./res/icon_128.jpg 为应用程序图标  

## 开发环境及工具
1. Python3.6 , Python3.7
2. Qt Designer
3. pyuic
4. pyrcc
5. Visual Studio Code
6. pycharm

## 程序说明
#### 根目录下程序
1. main.py为程序入口
2. Smartcar_SerialPort.py为程序主要文件。
Smartcar_SerialPort.MyMainWindow继承QWidget和由pyuic生成的布局文件Ui_SerialPort.UiForm，为程序的主界面。
3. widgetPainter.py中WidgetPainter为显示图像的组件，继承QWidget，
重写了keyPressEvent,mouseMoveEvent,paintEvent等事件处理函数
4. res_rc.py为方便程序导入res/res_rc.py而添加
5. parameter.py作用为解析parameter.json的参数，
6. GUI为图形界面布局文件，包括*.ui以及pyuic自动生成的.py文件
7. res为资源文件
8. OpenCV为待加入的opencv功能
#### GUI
1. Loading.ui为程序载入界面布局文件
2. SerialPort.ui为主界面布局文件
3. ParaList.ui为改参数ListWidget的每一个条目的布局文件
