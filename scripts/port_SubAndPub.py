#!/usr/bin/env python
import rospy
from serial_port.msg import header
from serial_port.msg import con
import serial
import time 

serialPort = "/dev/ttyUSB0"  
baudRate = 9600  
ser = serial.Serial(serialPort, baudRate, timeout=1)
print("port=%s ,b=%d" % (serialPort, baudRate))
time.sleep(1)

def callback(data):
    #rate = rospy.Rate(1)
    pub = rospy.Publisher('chatter', header, queue_size=10)
    #while not rospy.is_shutdown():
    get_str = ser.readline()
    get_str = get_str.strip()
    get_str = get_str.decode('utf-8','ignore') 
    #print(get_str)
    list_str = get_str.split(',')
    msg = header()
    data1 = int(list_str[0])
    data2 = int(list_str[1])
    data3 = int(list_str[2])
    msg.num1 = data1
    msg.num2 = data2
    msg.num3 = data3
    pub.publish(msg)
    print("I have read :" 
        "contral_data = "+str(data.con)+"\n")
    if data.con:
        ser.write("1\n") 
    else:
        ser.write("0\n") 
    #rate.sleep()
    time.sleep(1)
def SubscribeAndPublish():
    
    rospy.init_node('serial_data_contral', anonymous=True)
    rospy.Subscriber('contral_data', con, callback)
    rospy.spin()
   # rate = rospy.Rate(1) # 1hz


if __name__ == '__main__':
    try:
        SubscribeAndPublish()
    except rospy.ROSInterruptException:
        pass


