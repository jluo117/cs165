import 	hashlib
import 	time
def hashValue(inputStr):
	myHash = hashlib.md5()
	myHash.update(str.encode(inputStr))
	myHash.digest()
	return myHash.hexdigest()
def main():
	for i in range (26):
		iASCII = i + 97
		for j in range(26):
			jASCII = j + 97
			for k in range(26):
				kASCII = k + 97
				for l in range(26):
					lASCII = l + 97
					currentChar = chr(iASCII) + chr(jASCII) + chr(kASCII) + chr(lASCII)
					HashChar = chr(iASCII) + chr(jASCII) + chr(kASCII) + chr(lASCII)
					for i in range(1000):
						HashChar = hashValue(HashChar)
					print(currentChar + " " + HashChar)					
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))