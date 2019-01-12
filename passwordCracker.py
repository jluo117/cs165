
import  hashlib
import sys
import threading
salt = "hfT7jp2q"
salt = salt.encode("ASCII")
magic = b"$1$"
passwordList = []
solved = False
def ALTsum(inputStr):
	myHash = hashlib.md5()
	decodedInput = inputStr.encode("utf-8")
	myHash.update(decodedInput + salt + decodedInput)
	myHash.digest()
	return myHash.hexdigest()
#password p
def interSum(password,altSum):
	intersum = password.encode("utf-8") + magic + salt
	if len(password) > len(altSum):
		curIndex = 0
		cloneSum = altSum
		while len(cloneSum) < len(password):
			if curIndex >= len(cloneSum):
				curIndex = 0
			cloneSum += altSum[curIndex]
			curIndex += 1

	myBinary = str(format(len(password), "b"))
	if len(myBinary) < 4:
		needToADD = 4 - len(myBinary)
		for i in range(needToADD):
			myBinary = str(0) + myBinary
	for i in range(len(myBinary) - 1):
		print(myBinary[i])
		if myBinary[i] != 0:
			intersum += password[0].encode("utf-8")
		else:
			interSum += chr(0).encode("utf-8")
	myHash = hashlib.md5()
	myHash.update(intersum)
	myHash.digest() 
	return myHash.hexdigest()

def fastHash(intermedite,password,salt):
	#aab password+salt+password + aab
	theHash = intermedite + password
	myHash = hashlib.md5()
	myHash.update(theHash.encode("utf-8"))
	myHash.digest()
	intermedite = myHash.hexdigest()
	for i in range(1,1000):
		if i % 2 == 0:
			theHash = intermedite.encode("utf-8")
		else:
			theHash = password.encode("utf-8")
		if i % 3 != 0:
			theHash += salt
		if i % 7 != 0:
			theHash += password.encode("utf-8")
		if i % 2 == 0:
			theHash += password.encode("utf-8")
		else:
			theHash += intermedite.encode("utf-8")
		myHash = hashlib.md5()
		myHash.update(theHash)
		myHash.digest()
		intermedite = myHash.hexdigest()
		print(intermedite)
	return intermedite

def genHash(password):
	altsum = ALTsum(password)
	print(altsum)
	intersum = interSum(password,altsum)
	print(intersum)
	return fastHash(intersum,password,salt)

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
print("password".encode("utf-8"))
print("password".encode("utf-8")[0])
print(genHash("password"))
