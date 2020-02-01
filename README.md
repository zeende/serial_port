# serial_port
使用python编写arduino与ros之间串口通信（未使用rosserial库）
编译后 运行
roscore
rosrun serial_port talker.py  #此节点用于解析arduino从串口发来的数据，并发布。
rosrun serial_port listener.py #此节点订阅消息内容，并输出。
