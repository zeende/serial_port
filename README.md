# serial_port  
使用python编写arduino与ros之间串口通信（未使用rosserial库）  
  
2020.02.03
__更新为键盘控制，使用阿克曼运动模型__  
keyboard.py 用于读取键盘，并发布运动信息  
port_SubAndPub.py 用于订阅运动信息，通过串口发送到arduino，同时增加了读取串口数据的线程  
listener.py 此节点作用为订阅串口数据，打印在屏幕  
   
     
2020.02.02  
-----------------  
更新为双向通讯，自定义消息类型   
烧录arduino的contral2文件  
talker2.py  此节点作用为获取键盘数字输入并发布话题  
port_SubAndPub.py  此节点作用为订阅键盘数据话题，向串口发出控制指令，同时读取串口数据，并发布  
listener.py  此节点作用为订阅串口数据，打印在屏幕


2020.02.01  
------------------  
编译后 运行  
roscore  
rosrun serial_port talker.py  #此节点用于解析arduino从串口发来的数据，并发布。  
rosrun serial_port listener.py #此节点订阅消息内容，并输出。  
  
   
  
