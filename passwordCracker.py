
import  hashlib
import sys
import threading
salt = "hfT7jp2q"
salt = salt
magic = "$1$"
passwordList = []
solved = False
def ALTsum(inputStr):
	myHash = hashlib.md5()
	decodedInput = inputStr
	myHash.update((decodedInput + salt + decodedInput).encode("utf-8"))
	myHash.digest()
	print(myHash.hexdigest())
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
		print(bytearray([altSum.digest()[i % 16]]))
		print(([altSum.digest()[i % 16]]))
		#print(str(bytes(altSum[i % 16],"utf-8")))
	myHash = hashlib.md5()
	myHash.update((intersum))
	
	print(myHash.hexdigest())
	pwSize = len(password)
	while (pwSize != 0):
		if pwSize&1 == 0:
			intersum += password[0].encode("utf-8")
		else:
			intersum += chr(0).encode("utf-8")
		pwSize >>= 1 
	myHash = hashlib.md5()
	myHash.update((intersum))
	
	print(myHash.hexdigest())
	return  myHash

def fastHash(intermedite,password,salt):
	#aab password+salt+password + aab
	theHash = intermedite.digest() + password.encode("utf-8")
	myHash = hashlib.md5()
	myHash.update(theHash)
	myHash.digest()
	intermedite = myHash.hexdigest()
	for i in range(1,1000):
		if i % 2 == 0:
			theHash = intermedite.encode("utf-8")
		else:
			theHash = password.encode("utf-8")
		if i % 3 != 0:
			theHash += salt.encode("utf-8")
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
		#print(intermedite)
	return intermedite

def genHash(password):
	altsum = ALTsum(password)
	intersum = interSum(password,altsum,password)
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
print(genHash("password"))
