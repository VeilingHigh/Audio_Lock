import RPi.GPIO as GPIO
import time
import os

os.system('mplayer /home/pi/lock_audio/welcome.mp3')
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
def password_right_buzzer():
    for i in range(2):
        
        GPIO.output(21,1)
        time.sleep(0.1)
        GPIO.output(21,0)
        time.sleep(0.1)    

def password_input_buzzer():
    GPIO.output(21,1)
    time.sleep(0.2)
    GPIO.output(21,0)
def password_wrong_buzzer():
    GPIO.output(21,1)
    time.sleep(1)
    GPIO.output(21,0)	

def password_change_buzzer():
    for i in range(3):
        GPIO.output(21,1)
        time.sleep(0.1)
        GPIO.output(21,0)
        time.sleep(0.1) 
password=0
ppp=0
k=''
base=''
rows = [17, 25, 24, 23]
cols = [27, 18, 22]
keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']]
    
for row_pin in rows:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)	

for col_pin in cols:
    GPIO.setup(col_pin, GPIO.OUT)
def get_key():
    key = 0
    for col_num, col_pin in enumerate(cols):
        GPIO.output(col_pin, 1)
	time.sleep(0.005)
        for row_num, row_pin in enumerate(rows):
            if GPIO.input(row_pin):
                key = keys[row_num][col_num]
        GPIO.output(col_pin, 0)	
	time.sleep(0.005)
    return key
def sub_key():
    global ppp
    global k
    global password	
    k=''
    print 'please input your new password:\n' 
    os.system('mplayer /home/pi/lock_audio/np_first.mp3')
    while True:                   
        key=get_key()
        if key:            
            password_input_buzzer()
            k=k+key
            if len(k)==6:                
                password_change_buzzer()    
                a=k
                k=''
                print 'please input your new password again:\n'		     
                os.system('mplayer /home/pi/lock_audio/np_again.mp3')
            
            
                while True:
                    
                
                    
                    key=get_key()
                    if key:
                        
                        password_input_buzzer()
                        k=k+key
                        if len(k)==6:
                            
                            password_change_buzzer()
                            b=k
                            if a==b:
                                
                                password=a
                                open(ppp,'w').write(password)
                                print 'your new password is all set!'
                                os.system('mplayer /home/pi/lock_audio/new_password_set.mp3')
                            else:
                                print 'password is diffrent!'
                                os.system('mplayer /home/pi/lock_audio/diff.mp3')
                                sub_key()
                    if len(k)==6:                        
                         break
                    time.sleep(0.3)                    
        if len(k)==6:	    
	    break  
        time.sleep(0.3)        
def change_key():
    global k
    global password
    k=''
    print 'you can set your new password now!'
    os.system('mplayer /home/pi/lock_audio/input_new_password.mp3')
    sub_key()  
def users():
    print 'which user?'
    os.system('mplayer /home/pi/lock_audio/user1.mp3')
    while(True):
        global password
        global ppp
    
        key=get_key()
        if key :
            password_input_buzzer()
            if key=='1':
                p=open('/home/pi/password/password1.txt')
                ppp='/home/pi/password/password1.txt'
                password=p.read()
                p.close()
            if key=='2':
                p=open('/home/pi/password/password2.txt')
                ppp='/home/pi/password/password2.txt'
                password=p.read()
                p.close()
            if key=='3':
                p=open('/home/pi/password/password3.txt')
                ppp='/home/pi/password/password3.txt'
                password=p.read()
                p.close()
            if key=='4':
                p=open('/home/pi/password/password4.txt')
                ppp='/home/pi/password/password4.txt'
                password=p.read()
                p.close()
            if key=='5':
                p=open('/home/pi/password/password5.txt')
                ppp='/home/pi/password/password5.txt'
                password=p.read()
                p.close()
            if key=='6':
                p=open('/home/pi/password/password6.txt')
                ppp='/home/pi/password/password6.txt'
                password=p.read()
                p.close()
            os.system('mplayer /home/pi/lock_audio/user2.mp3')
        
            break    
def main():
    while True:
        global password
	global base
        key = get_key()
        if key :
            password_input_buzzer()
            base=base+key
            if base=='#'+password and len(base)==7:
                base='' 
                password_change_buzzer()
                change_key()  
                break
            if '#' in base and base!='#'+password and len(base)==7:
                print 'your original password is wrong!'
                base=''
                time.sleep(0.5)
                password_wrong_buzzer()
                os.system('mplayer /home/pi/lock_audio/original_wrong.mp3') 
                break
            if base==password and len(base)==6:
                print 'password is correct!'
                base=''
                time.sleep(0.5)	
                password_right_buzzer()
                os.system('mplayer /home/pi/lock_audio/password_right.mp3')
                break
            if '#' not in base and  base!=password and len(base)==6:  
                print 'password is wrong!'
                base=''
                time.sleep(0.5)
                password_wrong_buzzer()
                os.system('mplayer /home/pi/lock_audio/password_wrong.mp3')
                break
            if key=='*':
                print 'password is clear'
                base=''
                os.system('mplayer /home/pi/lock_audio/password_clear.mp3')
            if key=='#':
                print 'please input your original password:\n'
                base='#'
                os.system('mplayer /home/pi/lock_audio/input_old_password.mp3')
        time.sleep(0.3)
while True:
    users()
    main()	

        
