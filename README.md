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

传送的格式统一为字符串，上位机向下位机发送以奇数开始，下位机向上位机发送以偶数开始；以'\\1'结束

- 参数模式
    - 下位机向上位机发送以0xa0开始，格式为"\\xa0\[参数名\]\:\[参数值\]\\n\[参数位置\]:\[参数值(整数)\]\\n...\\1"

- 波形模式
    - 下位机向上位机发送以0xa8开始，格式为"\\xa8\[参数名\]\:\[参数值(浮点数)\]\\n\[参数位置\]:\[参数值(整数)\]\\n...\\1"

- 改参数模式
    - 上位机向下位机发送以0xb1开始，格式为"\\xb0\[参数位置\]:\[参数值(整数)\]"，
    成功后下位机向上位机发送0xb0\[参数值(整数)\]
    - 读取所有参数上位机向下位机发送以0xb3,
    成功后下位机向上位机发送0xb2\[参数位置\]:\[参数值(整数)\]\\n\[参数位置\]:\[参数值(整数)\]\\n...\\1
     
- 弹琴模式
    - 上位机向下位机发送以0xb9开始，格式为"\\xb9\[频率(整型，单位Hz)\]
    
#### 图像模式
单片机发送图像前必须先发送0x01 0xfe，表示图像的开始

## 文件说明
1. *.ui 为界面文件  
2. Ui_*.py pyuic编译.ui后的python文件  
3. CMD_Pyinstaller.bat 为 pyinstaller 打包 exe 指令  
4. ./res/icon_128.jpg 为应用程序图标 
5. parameter.json为调参模式下参数的数量，必须为32为整型。"name"可任意设置,"value"为上位机显示的初始值，可任意设置,"signed":为参数对应是否是有符号数 
6. setting.json为上位机默认初始值。
    "baude rate":默认波特率
    "send_hex":是否以16进制发送
    "receive_hex": 是否以16进制接收,
    "encode": 0:utf-8,1:GB2312
    "img_height":默认图像高度
    "img_width":默认图像宽度
    "img_type": 0:二进制图像,1:灰度图像
    "extra_14_bytes":是否接收额外14字节数据
    **是否接收额外14字节数据只能在该文件中改**
    "show_grid": 是否显示网格


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
