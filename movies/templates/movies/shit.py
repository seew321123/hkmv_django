# coding=utf-8
import random

a = input("这次你要出什么拳？")
b = random.randint(1,3)
if b == 1:
	print("电脑出了剪刀")
	if a =="石头":
		print("你出了石头，你赢了")
	elif a == "布":
		print("你出了布，你输了")
	else:
		print("你也出了剪刀，你们打平")
elif b == 2:
	print("电脑出了布")
	if a =="石头":
		print("你出了石头，你输了")
	elif a == "布":
		print("你也出了布，你们打平")
	else:
		print("你出了剪刀，你赢了")
else:
	print("电脑出了石头")
	if a =="石头":
		print("你也出了石头，你们打平")
	elif a == "布":
		print("你出了布，你赢了")
	else:
		print("你出了剪刀，你输了")