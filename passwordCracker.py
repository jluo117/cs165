from passlib.hash import md5_crypt
import  hashlib
import sys
import threading
salt = "hfT7jp2q"
passwordList = []
solved = False
def ALTsum(inputStr):
	myHash = hashlib.md5()
	myHash.update(str.encode(inputStr + salt + inputStr))
	myHash.digest()
	return myHash.hexdigest()

def interSum(password,altSum):
	intersum = password + magic + salt
	for i in range(len(altSum)):
		intersum += altSum
	myBinary = str(format(len(password), "b"))
	for i in myBinary:
		if i != 0:
			intersum += password[0]
		else:
			interSum += chr(ord('a') - 97)
	myHash = hashlib.md5()
	myHash.update(str.encode(interSum))
	myHash.digest() 
	return myHash.hexdigest()

def fastHash(intermedite,password,salt):
	theHash = None
	for i in range(1000):
		if i % 2 == 0:
			theHash = intermedite
		else:
			theHash = password
		if i % 3 != 0:
			theHash += salt
		if i % 7 != 0:
			theHash += password
		if i % 2 == 0:
			theHash += password
		else:
			theHash += intermedite
		myHash = hashlib.md5()
		myHash.update(str.encode(theHash))
		myHash.digest()
		intermedite = myHash.hexdigest()
def generatePW():
	for i in range(97,123):
		curPassWord = chr(i)
		passwordList.append(curPassWord)
		for j in range(97,123):
			curPassWord += chr(j)
			passwordList.append(curPassWord)
			for k in range(97,123):
				curPassWord += chr(k)
				passwordList.append(curPassWord)
				for l in range(97,123):
					curPassWord += chr(l)
					passwordList.append(curPassWord)
					for m in range(97,123):
						curPassWord += chr(m)
						passwordList.append(curPassWord)
						for n in range(97,123):
							curPassWord += chr(n)
							passwordList.append(curPassWord)
							for o in range(97,123):
								curPassWord += chr(o)
								passwordList.append(curPassWord)
								for p in range(97,123):
									curPassWord += chr(p)
									passwordList.append(curPassWord)
									print(passwordList)
									if solved:
										sys.exit()
print(chr(ord('a') - 97))