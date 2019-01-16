from hashlib import  md5
import  hashlib
import sys
import threading
salt = "hfT7jp2q"
salt = salt
magic = "$1$"
passwordList = []
solved = False
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
	myHash.digest()
	#print(myHash.hexdigest())
	return  myHash

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
	return intermedite.hexdigest()

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
