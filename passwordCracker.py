import  hashlib
import 	time
salt = "hfT7jp2q"
pw = "ti"
charTest = 't'
magic = "$1$"
pwlen = len(pw)
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
		if i == 0:
			
	myHash = hashlib.md5()
	myHash.update(str.encode(interSum))
	myHash.digest() 
	return myHash.hexdigest()


def isKthBitSet(n, k): 
    if n & (1 << (k - 1)): 
        return True
    else: 
        return  False
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

def cryptoHash(password):
	return fastHash(interSum(password,ALTsum(password)),password,salt) 

def CrackHash(value):
	for i in range (26):
		iASCII = i + 97
		for j in range(26):
			jASCII = j + 97
			for k in range(26):
				kASCII = k + 97
				for l in range(26):
					lASCII = l + 97
					for m in range (26):
						mASCII = m + 97
						for n in range (26):
							nASCII = n + 97
							currentChar = chr(iASCII) + chr(jASCII) + chr(kASCII) + chr(lASCII) + chr(mASCII) + chr(nASCII)
							HashChar = chr(iASCII) + chr(jASCII) + chr(kASCII) + chr(lASCII) + chr(mASCII) + chr(nASCII)
							for i in range(1000):
								HashChar = hashValue(HashChar)
											
start_time = time.time()
print (format(8, "b"))
print("--- %s seconds ---" % (time.time() - start_time))