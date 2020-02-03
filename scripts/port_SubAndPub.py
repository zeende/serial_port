#!/usr/bin/env python
import rospy
import std_msgs.msg
from serial_port.msg import header
from geometry_msgs.msg import Twist
import serial
import time 
import threading

serialPort = "/dev/ttyUSB0"  
baudRate = 9600  
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("port=%s ,b=%d" % (serialPort, baudRate))
time.sleep(1)
pub = rospy.Publisher('chatter', header, queue_size=1)



def thread_job():
    rospy.spin()

def callback(data):
    print("I have read :" 
         "Twist.linear.x = "+str(data.linear.x)+","
         "Twist.angular.z = "+str(data.angular.z)+"\n")
    str1=str(int(data.linear.x))
    str2=str(int(data.angular.z))
    ser.write("%s,%s"%(str1,str2))
    time.sleep(0.2)
    # print("%d,%d"%(data.linear.x,data.angular.z))


def SubscribeAndPublish():
    rospy.init_node('serial_data_contral', anonymous=True)
    rospy.Subscriber('~/car/cmd_vel', Twist, callback,queue_size=1,buff_size=52428800)
    # rospy.spin()
    rate = rospy.Rate(5)
    add_thread = threading.Thread(target = thread_job)
    add_thread.start()

    while not rospy.is_shutdown():
        
        get_str = ser.readline()
        get_str = get_str.strip()
        get_str = get_str.decode('utf-8','ignore') 
        print(get_str)
        print("######\n")
        list_str = get_str.split(',')
        msg = header()
        # data1 = int(list_str[0])
        # data2 = int(list_str[1])
        # data3 = int(list_str[2])
        # msg.num1 = data1
        # msg.num2 = data2
        # msg.num3 = data3
        # pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        SubscribeAndPublish()
    except rospy.ROSInterruptException:
        pass


########################