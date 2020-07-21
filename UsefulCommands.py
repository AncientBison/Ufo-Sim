import math
import sys
import time

Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
Bold = "\033[1m"
Yellow = "\033[1;38m"
Clear = "\033[3J\033[H\033[2J"
sp = 0.00
fp = 0.4

def sprint(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(sp)
  print()

def fprint(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(fp)
  print()


def ask(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(sp)
	return input()

	