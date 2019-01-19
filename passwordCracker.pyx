#$1$hfT7jp2q$G3yf0NUx7mUkX.LIFWQxN.
from hashlib import  md5
import  hashlib
import sys
import threading
#import numpy as np
import twilio
from twilio.rest import Client
import threading
from queue import *
import 	time
from multiprocessing import Process
from threading import Thread
import os

#GlobalQueue = Queue()
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
_c_digest_offsets = (
    (0, 3), (5, 1), (5, 3), (1, 2), (5, 1), (5, 3), (1, 3),
    (4, 1), (5, 3), (1, 3), (5, 0), (5, 3), (1, 3), (5, 1),
    (4, 3), (1, 3), (5, 1), (5, 2), (1, 3), (5, 1), (5, 3),
    )
def ALTsum(inputStr):
	myHash = hashlib.md5()
	decodedInput = inputStr
	myHash.update((decodedInput + salt + decodedInput).encode("utf-8"))
	myHash.digest()
	#print(myHash.hexdigest())
	return myHash
#password p
def interSum(password,altSum,encodedPassword):
	intersum = password + magic + salt
	if len(password) > altSum.digest_size:
		curIndex = 0
		cloneSum = altSum
		cloneSumLengeth = int (cloneSum.digest_size)
		# print(cloneSumLengeth)
		# print(len(password))
		# print(password)
		while cloneSumLengeth < len(password):
			if curIndex >= cloneSumLengeth:
				curIndex = 0
				cloneSum += altSum[curIndex]
				curIndex += 1
				cloneSumLengeth += 1
		altSum = cloneSum
	intersum = intersum.encode("utf-8")
	for i in range(len(password)):
		intersum += bytearray([altSum.digest()[i % 16]])
		#print(([altSum.digest()[i % 16]]))
	myHash = hashlib.md5()
	myHash.update((intersum))
	
	#print(myHash.hexdigest())
	pwSize = len(password)
	while (pwSize != 0):
		if pwSize&1 == 0:
			intersum += password[0].encode("utf-8")
		else:
			intersum += chr(0).encode("utf-8")
		pwSize >>= 1 
	myHash = hashlib.md5()
	myHash.update((intersum))
	#myHash.digest()
	#print(myHash.hexdigest())
	return  myHash
def unsigned(n):
	return n & 0xFFFFFFFF

def fastHash(intermedite,password,salt):
	#aab password+salt+password + aab
	#print(intermedite)
	
	for i in range(1000):
		intermediteHash = intermedite.digest()
		newSum = hashlib.md5()
		if i % 2 == 0:
			newSum.update(intermediteHash)
		else:
			newSum.update(password.encode("utf-8"))
		if i % 3 != 0:
			newSum.update(salt.encode("utf-8"))
		if i % 7 != 0:
			newSum.update(password.encode("utf-8"))
		if i % 2 == 0:
			newSum.update(password.encode("utf-8"))
		if i % 2 != 0:
			newSum.update(intermediteHash)
		intermedite = newSum
	return intermedite

def reorder(fasthash):
	result = []
	v= unsigned(0)
	bits = unsigned(0)
	for i in md5CryptSwaps:
		v |= fasthash.digest()[i] << bits
		#print(unsigned(fasthash.digest()[i]))
		#print(bin (fasthash.digest()[i]))
		#print(v)
		#print((fasthash.digest()[i]))
		bits += 8
		while bits > 6:
			result.append(CryptBase[v&0x03f])
			v >>= 6
			bits += -6
	result.append(CryptBase[v&0x3f])
	return result
	
def aryToStr(ary):
	returnStr = ""
	for i in ary:
		returnStr += i
	return magic +  salt+ '$' + returnStr

def genHash(password):
	altsum = ALTsum(password)
	intersum = interSum(password,altsum,password)
	fasthash = fastHash(intersum,password,salt)
	reorderResult =  reorder(fasthash)
	return aryToStr(reorderResult)
def threadHandling():
	for i in range(6):
		newThread = Thread(target = consumer_thread)
		threadStack.append(newThread)
		newThread.start()
	for i in range(len(threadStack)):
		if threadStack[i].isAlive():
			if len(passwordList) < 200:
				time.sleep(5)
				break
			else:
				time.sleep(20)
				continue
	while len(threadStack) != 0:
		threadStack.pop()

def generatePW(targetHash):
	startChar = ord('c')
	for i in range(startChar,122):
		curPassWord = chr(i)
		passwordList.append(curPassWord)
		#print(curPassWord)
		baseCase2(curPassWord,targetHash)
def baseCase2(curPassWord,targetHash):
	for i in range(97,123):
		newWord = curPassWord + chr(i)
		passwordList.append(newWord)
		recursiveBuild(newWord)
		print(newWord)
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
	
	while not len(passwordList) > 0:
		curPass = passwordList.pop()
		result = genHash(curPass)
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
	for i in range (ord('f'),ord('z') + 1):
		curPW = 'c' + chr(i)
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
	quickFix()
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

#start_time = time.time()
main()
#print("--- %s seconds ---" % (time.time() - start_time))