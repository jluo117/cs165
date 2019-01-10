import 	hashlib

def hashValue(inputStr):
	myHash = hashlib.md5()
	myHash.update(str.encode(inputStr))
	myHash.digest()
	return myHash.hexdigest()
rawText = "Hello World"
newRawText = "Hello World"
for i in range(1000):
	rawText = hashValue(rawText)
	newRawText = hashValue(newRawText)
	print(rawText)
	print(newRawText)
	if rawText != newRawText:
		raise ("abort")
if rawText == newRawText:
	print("good")

