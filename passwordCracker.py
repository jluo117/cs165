import 	hashlib
import 	time
def hashValue(inputStr):
	myHash = hashlib.md5()
	myHash.update(str.encode(inputStr))
	myHash.digest()
	return myHash.hexdigest()
def main():
	rawText = "zyaj"
	for i in range(1000):
		rawText = hashValue(rawText)
	for i in range (27):
		iASCII = i + 97
		for j in range(27):
			jASCII = j + 97
			for k in range(27):
				kASCII =  k + 97
				for l in range(27):
					lASCII = l + 97
					currentChar = chr(iASCII) + chr(jASCII) + chr(kASCII) + chr(lASCII)
					for i in range(1000):
						currentChar = hashValue(currentChar)
					if currentChar == rawText:
						print("done")
						return
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))