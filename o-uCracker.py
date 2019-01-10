import 	hashlib
import 	time
def hashValue(inputStr):
	myHash = hashlib.md5()
	myHash.update(str.encode(inputStr))
	myHash.digest()
	return myHash.hexdigest()
def main():
	for i in range (7):
		iASCII = i + 97 + 14
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
							print(currentChar + " " + HashChar)					
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))