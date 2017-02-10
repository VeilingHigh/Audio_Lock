# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:10:47 2016

@author: VeilingHigh
"""   
from socket import *
host = '192.168.1.104'
port = 8889
bufsiz =1024
addr = (host, port)

def SendComand(cmd):
  s=socket(AF_INET, SOCK_STREAM)
  s.connect(addr)
  s.send(cmd)
  s.close()
  
import getpass
n=0
flag=0
color=0
p=open('/storage/emulated/0/A/password.txt')
password=p.read()
p.close()
a=0
b=0
def set_password():
    global a
    global b
    global password
    global color
    color='green_forever'
    SendComand(color)
    a=getpass.getpass('请输入您的新密码:\n')
    b=getpass.getpass('请再输入一次:\n')
    if a==b:
        password=a
        open('/storage/emulated/0/A/password.txt','w').write(password)
        print '新密码设置成功!'
        color='red'
        SendComand(color)        
    else:
        print '两次输入的新密码不一致，请重新输入!'
        set_password()    
def change_password(state):
    global a
    global b
    global color
    global password
    if state=='1':
        p=getpass.getpass('请输入您的原始密码:\n')
        if password==p:
            set_password()
        else:
            print '原始密码输入错误!'
            color='red'
            SendComand(color)
    else:
        pass
def input_password():
    global password
    global color
    global n
    global flag
    pp=getpass.getpass('请输入您的密码:\n')
    if pp==password:       
        print '密码正确!'
        color='green'
        SendComand(color)
        flag=1
    else:
        if n<4:
            print '密码错误！请重新输入!'
            color='red'
            SendComand(color)
        flag=0
        n=n+1
        if n==5:
            print '您已经输入密码错误多次，我们已通知警方！'
            color='yellow'
            SendComand(color)
while(True):
    h=getpass.getpass('您想重置您的密码吗?(是:1|否:0)\n:')
    change_password(h)
    input_password()
    if flag==1 or n==5:
        break
    
        
        
        
        
 
        
        
