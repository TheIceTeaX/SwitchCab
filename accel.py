#!/usr/bin/python
import smbus;import math;from time import sleep;import RPi.GPIO as GPIO
#Valeur de declanchement des relay.
N_TO_DOWN = (-12000)    # Z Casser la vitre
N_TO_LEFT = (+12000)     # Y Nudge vers la gauche
N_TO_RIGHT= (-12000)     # Y Nudge vers la droite
N_TO_UP   = (+9000)     # X Nudge en avant
N_TO_BACK = (-9000)    # X Nudge en arr si besoin... ou pas LOL 

CALIBRAGEREAL_Y = (0)
CALIBRAGEREAL_X = (0) 
CALIBRAGEREAL_Z = (0)

# pour afficher les valeur X et Y pour le parametrage
# 0= pas de test , 1= test
# les relay ne fonctionnent mal en test=1
test=0

# calibration automatique
# 0= pas de calibration 1= calibration a chaque allumage
CALIBR=1

GPIO.setmode(GPIO.BOARD);GPIO.setwarnings(False)
x=1

LED29 = 29;GPIO.setup(LED29,GPIO.OUT);GPIO.output(LED29,GPIO.LOW);sleep(0.1);GPIO.output(LED29,GPIO.HIGH);sleep(0.1)
LED31 = 31;GPIO.setup(LED31,GPIO.OUT);GPIO.output(LED31,GPIO.LOW);sleep(0.1);GPIO.output(LED31,GPIO.HIGH);sleep(0.1)
LED33 = 33;GPIO.setup(LED33,GPIO.OUT);GPIO.output(LED33,GPIO.LOW);sleep(0.1);GPIO.output(LED33,GPIO.HIGH);sleep(0.1)
LED35 = 35;GPIO.setup(LED35,GPIO.OUT);GPIO.output(LED35,GPIO.LOW);sleep(0.1);GPIO.output(LED35,GPIO.HIGH);sleep(0.1)
LED37 = 37;GPIO.setup(LED37,GPIO.OUT);GPIO.output(LED37,GPIO.LOW);sleep(0.1);GPIO.output(LED37,GPIO.HIGH);sleep(0.1)

power_mgmt_1 = 0x6b;power_mgmt_2 = 0x6c   
def read_byte(reg):
    return bus.read_byte_data(address, reg) 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val   
def read_word_2c2(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1 + CALIBRAGEREAL_Y )
    else:
        return val
def read_Y(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1 + CALIBRAGEREAL_Y )
    else:
        return val   
def read_X(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1 + CALIBRAGEREAL_X )
    else:
        return val   
def read_Z(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1 + CALIBRAGEREAL_Z )
    else:
        return val
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
bus = smbus.SMBus(1);address = 0x68;bus.write_byte_data(address, power_mgmt_1, 0)

if CALIBR == 1 :
    print ("CALIBRATION 1 ne pas bouger");CX1 = read_word_2c(0x3b);CY1 = read_word_2c(0x3d);CZ1 = read_word_2c(0x3f)
    print ("CALIBRATION", CX1 , CY1 ,CZ1);sleep (1.0)
    print ("CALIBRATION 2 ne pas bouger");CX2 = read_word_2c(0x3b);CY2 = read_word_2c(0x3d);CZ2 = read_word_2c(0x3f)
    print ("CALIBRATION", CX2 , CY2 ,CZ2);sleep (1.0)
    print ("CALIBRATION 3 ne pas bouger");CX3 = read_word_2c(0x3b);CY3 = read_word_2c(0x3d);CZ3 = read_word_2c(0x3f)
    print ("CALIBRATION", CX3 , CY3 ,CZ3);sleep (1.0)
    print ("CALIBRATION 4 ne pas bouger");CX4 = read_word_2c(0x3b);CY4 = read_word_2c(0x3d);CZ4 = read_word_2c(0x3f)
    print ("CALIBRATION", CX4 , CY4 ,CZ4);sleep (1.0)
    print ("CALIBRATION 5 ne pas bouger");CX5 = read_word_2c(0x3b);CY5 = read_word_2c(0x3d);CZ5 = read_word_2c(0x3f)
    print ("CALIBRATION", CX5 , CY5 ,CZ5);sleep (1.0)
    print ("CALIBRATION 6 ne pas bouger");CX6 = read_word_2c(0x3b);CY6 = read_word_2c(0x3d);CZ6 = read_word_2c(0x3f)
    print ("CALIBRATION", CX6 , CY6 ,CZ6);sleep (1.0)
    print ("CALIBRATION 7 ne pas bouger");CX7 = read_word_2c(0x3b);CY7 = read_word_2c(0x3d);CZ7 = read_word_2c(0x3f)
    print ("CALIBRATION", CX7 , CY7 ,CZ7);sleep (1.0)
    print ("CALIBRATION 8 ne pas bouger");CX8 = read_word_2c(0x3b);CY8 = read_word_2c(0x3d);CZ8 = read_word_2c(0x3f)
    print ("CALIBRATION", CX8 , CY8 ,CZ8);sleep (1.0)
    print ("CALIBRATION 9 ne pas bouger");CX9 = read_word_2c(0x3b);CY9 = read_word_2c(0x3d);CZ9 = read_word_2c(0x3f)
    print ("CALIBRATION", CX9 , CY9 ,CZ9);sleep (1.0)
    print ("CALIBRATION 10 ne pas bouger");CX10 = read_word_2c(0x3b);CY10 = read_word_2c(0x3d);CZ10 = read_word_2c(0x3f)
    print ("CALIBRATION", CX10 , CY10 ,CZ10);sleep (1.0)
    CX11 = CX1 + CX2 + CX3 + CX4 + CX5 + CX6 + CX7 + CX8 + CX9 + CX10;CX12 = CX11/10
    print ("CALIBRATION X =",CX12);CY11 = CY1 + CY2 + CY3 + CY4 + CY5 + CY6 + CY7 + CY8 + CY9 + CY10
    CY12 = CY11/10;print ("CALIBRATION Y =",CY12)
    CZ11 = CZ1 + CZ2 + CZ3 + CZ4 + CZ5 + CZ6 + CZ7 + CZ8 + CZ9 + CZ10
    CZ12 = CZ11/10;print ("CALIBRATION Z =",CZ12)
    
    if CX12 >= 0 :
        CALIBRAGEREAL_X = 0 - CX12        
    if CX12 <= 0 :
        CALIBRAGEREAL_X = CX12 * -1
    if CY12 >= 0 :
        CALIBRAGEREAL_Y = 4
    if CY12 <= 0 :
        CALIBRAGEREAL_Y = CY12 * -1
    #if CZ12 >= 0 :
    #    CALIBRAGEREAL_Z = 2
    #if CZ12 <= 0 :
    #    CALIBRAGEREAL_Z = 3
        
    X_out = read_word_2c(0x3b) + CALIBRAGEREAL_X
    Y_out = read_word_2c(0x3d) + CALIBRAGEREAL_Y
    Z_out = read_word_2c(0x3f) + CALIBRAGEREAL_Z 
    print ( "valeurs retenue de calibration      : X= ",CALIBRAGEREAL_X,"    Y= ",CALIBRAGEREAL_Y,"    Z= ",CALIBRAGEREAL_Z)
    print ( "valeurs accel brut                  : X= ",read_X (0x3b),"    Y=",read_Y(0x3d),"    Z=",read_Z(0x3f) )
    print ( "valeurs accel calibré + ou - 300 OK : X= ",X_out,"    Y=",Y_out,"    Z=",Z_out )
    print ( "la valeur de Z doit etre a envrion 14000 cette valeurs nest pas calibrée" )
    GPIO.output(LED29, GPIO.LOW) ;sleep (0.1);GPIO.output(LED29, GPIO.HIGH) ;sleep (0.1)
    GPIO.output(LED29, GPIO.LOW) ;sleep (0.1);GPIO.output(LED29, GPIO.HIGH) ; sleep (0.2)
    x=0
    
while x==0 :
    #led.on()
    X_out = read_word_2c(0x3b) + CALIBRAGEREAL_X
    Y_out = read_word_2c(0x3d) + CALIBRAGEREAL_Y
    Z_out = read_word_2c(0x3f) + CALIBRAGEREAL_Z  
#<<<<<<<<
    if Y_out > N_TO_LEFT : #or REAL_Y > N_TO_LEFT / 2 :
        print (" <-- Nudge to left","Valeur enregistrée Y=",Y_out,"Valeur debug",read_Y(0x3d),)
        GPIO.output(LED29, GPIO.LOW) ;sleep (0.1);GPIO.output(LED29, GPIO.HIGH);sleep (0.25)
        
#>>>>>>>>
    elif Y_out < N_TO_RIGHT : # or REAL_Y < N_TO_RIGHT / 2 :
        print (" --> Nudge to right","Valeur enregistrée Y=",Y_out,"Valeur debug",read_Y(0x3d),)
        GPIO.output(LED31, GPIO.LOW) ;sleep (0.1);GPIO.output(LED31, GPIO.HIGH);sleep (0.25)

#^^^^^^^^            
    elif X_out > N_TO_UP :
        print (" ^^^ Nudge avant. Valeur enregistrée X=",X_out,"Valeur debug",read_X(0x3b))
        GPIO.output(LED33, GPIO.LOW) ;sleep (0.1);GPIO.output(LED33, GPIO.HIGH);sleep (0.25)
        
    elif X_out < N_TO_BACK:
        print (" !!! Nudge arr Valeur enregistrée X=",X_out,"Valeur debug",read_X(0x3b))
        GPIO.output(LED35, GPIO.LOW) ;sleep (0.10);GPIO.output(LED35, GPIO.HIGH);sleep (0.25)
        
    elif Z_out < N_TO_DOWN:
        print ("tu va briser la vitre enfoiré . Valeur enregistrée Z=",Z_out,"Valeur debug",read_Z(0x3f))
        GPIO.output(LED29, GPIO.LOW) ; sleep (0.1)
        GPIO.output(LED29, GPIO.HIGH) ; sleep (0.1)
        GPIO.output(LED31, GPIO.LOW) ; sleep (0.1)
        GPIO.output(LED31, GPIO.HIGH) ; sleep (0.1)
        GPIO.output(LED33, GPIO.LOW) ; sleep (0.1)
        GPIO.output(LED33, GPIO.HIGH) ; sleep (0.1)
    
    elif test == 1 :
        print ( "valeur accel brut    : x" , read_X (0x3b),"y", read_Y(0x3d),"z", read_Z(0x3f) )
        print ( "valuer accel calibre : x" , X_out,"y", Y_out,"z", Z_out )
        sleep (2)