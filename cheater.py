from passlib.hash import md5_crypt
#import  passwordCracker
#from hashlib import  md5
#import  hashlib
import sys
import threading
#import numpy as np
import twilio
from twilio.rest import Client
import threading
from threading import Thread
from queue import *
import 	time    # this comes from a compiled binary
count = 0
threadStack = []
solved = ["done"]
doneValue = set()
CryptBase = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
md5CryptSwaps = [12, 6, 0, 13, 7, 1, 14, 8, 2, 15, 9, 3, 5, 10, 4, 11]
salt = "hfT7jp2q"
salt = salt
magic = "$1$"
passwordList = []
targetHash = "$1$hfT7jp2q$B96oRTlE0yZWjRx7qoO920"
def threadHandling():
	for i in range(6):
		newThread = Thread(target = consumer_thread)
		newThread.start()		
		threadStack.append(newThread)
	for i in range(len(threadStack)):
		if threadStack[i].isAlive():
			if len(passwordList) < 200:
				break
			else:
				threadStack[i].join()
	while len(threadStack) != 0:
		threadStack.pop()

def generatePW(targetHash):
	startChar = ord('e')
	for i in range(startChar,122):
		curPassWord = chr(i)
		passwordList.append(curPassWord)
		#print(curPassWord)
		baseCase2(curPassWord,targetHash)
def baseCase2(curPassWord,targetHash):
	for i in range(97,123):
		newWord = curPassWord + chr(i)
		print(newWord)
		passwordList.append(newWord)
		recursiveBuild(newWord)
		threadHandling()
		
		

def recursiveBuild(curPassWord):
	if len(curPassWord) == 6:
		return 
	for i in range(97,123):
		newWord = curPassWord + chr(i)
		passwordList.append(newWord)
		recursiveBuild(newWord)



def consumer_thread():
	#print(myPWD)
	print("cracking")
	print(len(passwordList))
	while len(passwordList) > 0:

		curPass = passwordList.pop()
		#print(curPass)
		result = md5_crypt.using(salt = "hfT7jp2q").hash(curPass)
		if str(result) == str(targetHash):
			#print(result)
			print(curPass)
			sendMsg(curPass)
			solved.pop()
			sys.exit()
			return 
	print("Thread finished")
	#sys.exit()

def sendMsg(msg):
	account_sid = "ACe704104c6f665965aeb765eea2a1502a"
	auth_token = "2aa7630860a97a3fb9de4ab53a94abc4"
	client = Client(account_sid, auth_token)
	client.api.account.messages.create(
        to="+14158109857",
        from_="+15108228362",
        body=msg,
        )
def quickFix():
	
	#curPW = 'c'
	for i in range (ord('g'),ord('z') + 1):
		curPW = 'd' + chr(i)
		passwordList.append(curPW)
	#start_time = time.time()

		print(curPW)
		#print(len(passwordList))
		recursiveBuild(curPW)
		print(len(passwordList))
		threadHandling()
def main():
	#testHash = "$1$hfT7jp2q$B96oRTlE0yZWjRx7qoO920"
	#targetHash = testHash
	#quickFix()
	generatePW(targetHash)
	for t in threadStack:
		t.join()
	#generatePW(targetHash)

# def notThreading():
# 	start_time = time.time()
# 	targetHash = genHash("aaaaz")
# 	#print(targetHash)
# 	passwordList.put("asdasdasd")
# 	passwordList.put("fdsafdsafsadf")
# 	passwordList.put("aaaaz")
# 	passwordList.put("fdsafdsafsadf")
# 	myThread = threading.Thread( target = consumer_thread(targetHash))
# 	myThread.start()
# 	myThread2 = threading.Thread( target = consumer_thread(targetHash))
# 	myThread2.start()
main()