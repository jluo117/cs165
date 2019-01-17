#$1$hfT7jp2q$G3yf0NUx7mUkX.LIFWQxN.
from hashlib import  md5
import  hashlib
import sys
import threading
import numpy as np
import twilio
from twilio.rest import Client
import threading
from queue import *
solved = ["done"]
CryptBase = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
md5CryptSwaps = [12, 6, 0, 13, 7, 1, 14, 8, 2, 15, 9, 3, 5, 10, 4, 11]
salt = "hfT7jp2q"
salt = salt
magic = "$1$"
passwordList = Queue()
targetHash = None
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
		while len(cloneSum) < len(password):
			if curIndex >= len(cloneSum):
				curIndex = 0
			cloneSum += altSum[curIndex]
			curIndex += 1
		altSum = cloneSum
	intersum = intersum.encode("utf-8")
	for i in range(len(password)):
		intersum += bytearray([altSum.digest()[i % 16]])
		#print(str(bytes(altSum[i % 16],"utf-8")))
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
def generatePW():
	for i in range(97,123):
		curPassWord = chr(i)
		passwordList.put(curPassWord)
		for j in range(97,123):
			curPassWord += chr(j)
			passwordList.put(curPassWord)
			for k in range(97,123):
				curPassWord += chr(k)
				passwordList.put(curPassWord)
				for l in range(97,123):
					curPassWord += chr(l)
					passwordList.put(curPassWord)
					for m in range(97,123):
						curPassWord += chr(m)
						passwordList.put(curPassWord)
						for n in range(97,123):
							curPassWord += chr(n)
							passwordList.put(curPassWord)
							for o in range(97,123):
								curPassWord += chr(o)
								passwordList.put(curPassWord)
								for p in range(97,123):
									curPassWord += chr(p)
									passwordList.put(curPassWord)
									if solved:
										sys.exit()
def consumer_thread(targetHash):

	while not len(solved) == 0:
		#print(targetHash)
		myPWD = passwordList.get()
		#print(myPWD)
		result = genHash(myPWD)
		#print(result)
		if str(result) == str(targetHash):
			#print(result)
			print(myPWD)
			sendMsg(myPWD)
			solved.pop()
	sys.exit()

def sendMsg(msg):
    account_sid = "ACe704104c6f665965aeb765eea2a1502a"
    auth_token = "2aa7630860a97a3fb9de4ab53a94abc4"

    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to="+14158109857",
        from_="+15108228362",
        body=msg,
        )

def main():
	testHash = "$1$hfT7jp2q$B96oRTlE0yZWjRx7qoO920"
	targetHash = testHash
	t1 = threading.Thread( target = generatePW())
	t1.start()
	for i in range(7):
		myThread = threading.Thread( target = consumer_thread(targetHash))
		myThread.start()
def notThreading():
	targetHash = genHash("aaaaz")
	#print(targetHash)
	passwordList.put("asdasdasd")
	passwordList.put("fdsafdsafsadf")
	passwordList.put("aaaaz")
	passwordList.put("fdsafdsafsadf")
	myThread = threading.Thread( target = consumer_thread(targetHash))
	myThread.start()
	myThread2 = threading.Thread( target = consumer_thread(targetHash))
	myThread2.start()
main()
