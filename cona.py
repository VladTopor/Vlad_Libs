import time
import os
WHITE = "\033[1;37m"
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = ORANGE = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;30m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
BRICK = "█"
TICK = "✓"
CROSS = "✕"
LOADS = ["-","/","-","\\","|","/"]
def cprint(text,color=WHITE,end="\n"):
	print(color+text,end=end)
def printto(text,x,y,color=WHITE):
	print(f"\033[{x};{y}H{color}{text}")
def clear():
	print("\n"*os.get_terminal_size().lines)
class Loading:
	def __init__(self,x,y):
		self.index = 0
		self.x = x
		self.y = y
		self.loops = 0
		printto(LOADS[self.index],x,y)
	def update(self,delay):
		time.sleep(delay)
		self.index+=1
		self.loops+=1
		if self.index == 6:
			self.index=0
		printto(LOADS[self.index],self.x,self.y)
class ProgressBar:
	def __init__(self,x,y,sp=False):
		self.x = x
		self.y = y
		self.sp = sp
		printto("["+"_"*10+"] 0%",x,y)
	def set(self,value):
		if value > 100:
			value = 100
		per = value
		value/=10
		if self.sp == False:
			printto(BRICK*int(value),self.x,self.y+1,"")
		else:
			printto(f"{BRICK*int(value)}{'_'*(10-(int(value)))}] {per}%",self.x,self.y+1,"")
if __name__ == "__main__":
	import sys
	if len(sys.argv) == 1:
		pass
	elif len(sys.argv) == 2:
		if sys.argv[1] == "--clear":
			clear()
		else:
			cprint("Usage: cona --clear", RED)
	else:
		cprint("Usage: cona --clear",RED)
