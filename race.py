import os
from time import sleep
import random

class colors:
    BLACK    = '\33[30m'
    RED      = '\33[31m'
    GREEN    = '\33[32m'
    YELLOW   = '\33[33m'
    BLUE     = '\33[34m'
    VIOLET   = '\33[35m'
    BEIGE    = '\33[36m'
    WHITE    = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'

__bosluk=0
os.system("clear")
_x_win = 0
_y_win = 0
_x_color = colors.BLUE
_y_color = colors.BLUE
round=0
max_round =10

def agac(_bosluk,_color):
	yildiz=1
	bosluk=10
	for a in range(11):
		print(_color + _bosluk*" ",end="")
		print(_color + bosluk*" ",end="")
		print(_color + yildiz*"*")
		bosluk-=1
		yildiz+=2
		if(a >= 10):
			print(_color + _bosluk*" "+"         | |")
			print(_color + _bosluk*" "+"         | |")
			print(_color + _bosluk*" "+"      ---------")
			print(colors.END)
			break
while round<max_round:
	round+=1
	_x=0
	_y=0
	while(_x <= 50):
		print(colors.GREENBG + "x : "+str(_x_win)+"  ")
		print("y : "+str(_y_win) + colors.END+"  ")
		if(_x_win > _y_win):
			_x_color,_y_color = colors.VIOLET,colors.RED
		elif(_x_win == _y_win):
			_x_color,_y_color = colors.WHITE,colors.WHITE
		else:
			_x_color,_y_color = colors.RED,colors.VIOLET
		agac(_x,_x_color)
		print(colors.END)
		print("\n--------------------------------------------------------------------------------------------------------")
		print("\n--------------------------------------------------------------------------------------------------------")
		agac(_y,_y_color)
		sleep(0.3)
		os.system("clear")
		_x+=random.randint(0,20)
		_y+=random.randint(0,20)
	if(_x > 50 or _y > 50):
		if(_x > _y):
			_x_win +=1
		else:
			_y_win +=1

if(_x_win > _y_win):
	winner ="x"
	text="kazanan : "+winner
elif(_x_win == _y_win):
	winner =0
	text="berabere"
else:
	winner="y"
	text="kazanan : "+winner
print(colors.WHITE+"\n\n    Puan Durumu ")
print("----------------")
print("  x = "+str(_x_win))
print("  y = "+str(_y_win))
print("\n"+colors.WHITEBG+colors.BLACK+text+colors.END+"\n")

"""
          *          
         ***         
        *****        
       *******       
      *********      
     ***********     
    *************    
   ***************   
  *****************  
 ******************* 
         ||          
         ||          
       ------        
                     
                     

"""

