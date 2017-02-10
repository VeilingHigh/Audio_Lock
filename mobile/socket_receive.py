# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(18,True) 
from socket import *  
import time
def green():
    GPIO.output(17,True)
    GPIO.output(18,False)
    time.sleep(3)
    GPIO.output(17,False)
    GPIO.output(18,True)    
def red():
    GPIO.output(18,True)
    GPIO.output(17,False)	
    
def yellow():
    GPIO.output(27,True)
    time.sleep(3)
    GPIO.output(27,False)
def green_forever():
    GPIO.output(17,True)
    GPIO.output(18,False)  
commands ={'green':green,  
  'red':red,   
  'yellow':yellow,
  'green_forever':green_forever
}  
  
def execute(command):     
    print command  
    commands[command]()  
  
HOST ='192.168.1.104'
PORT = 8889  
s= socket(AF_INET, SOCK_STREAM)  
s.bind((HOST, PORT))  
s.listen(1)  
print ('listening on 8889')  
while 1:  
    conn, addr = s.accept()  
    print ('Connected by:', addr)  
    while 1:  
            command= conn.recv(1024).replace('\n','')  
            if not command:break  
            execute(command)  
    conn.close()
