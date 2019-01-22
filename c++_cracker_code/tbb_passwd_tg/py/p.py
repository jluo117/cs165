#$1$hfT7jp2q$G3yf0NUx7mUkX.LIFWQxN.
import hashlib
import sys
import threading
import time
import os

teamsDict =	{
	"/sDfNdP2e3OCxg2zGq1FK0" : "team0",
	"8rU1qXqPJfSiwL8uts982." : "team1",
	"v8XH/MrpaYdagdMgM4yKc." : "team2",
	"ol/pX72DmNxt/abvoCwZO0" : "team3",
	"g.L45izUKySxx0yWx8.xn1" : "team4",
	"QCP2BGfZm484hn6SovY1Q1" : "team5",
	"eZhkYfvJ3wbqT1h/iIJLq/" : "team6",
	"u3zPkglU5aB4J3suCZ3yA/" : "team7",
	"KyYIVk1b7GbGnSPxu1q911" : "team8",
	"qNp7RyvWVdXKfCP9KaodW/" : "team9",
	"wh5MlWjVniktm6zI5jpf3." : "team10",
	"Y/iA7VyPo6sV6gI9asORk/" : "team11",
	"Mf6vrrDQCqXg8xroT.laC." : "team12",
	"KqcshpOfHc7VFTtiIZHPe1" : "team13",
	"hcTYI5BM0fCoukdK0pZUd." : "team14",
	"/0Qej/r2CciuyRNPWMme41" : "team15",
	"oUhZwoeUK8XPPXOxVC2cB0" : "team16",
	"XbuTW3pLaiV7Q18a6euwb0" : "team17",
	"JU0X9xRQyTWTWY59e3Iqj1" : "team18",
	"DGnUWXz9kUxGmqygY8tSH." : "team19",
	"xjJ9S81r4kwLxYDNQ70tZ0" : "team20",
	"9oeZEUhDvm5wy1Z6jWO2x/" : "team21",
	"rq9TIlJdpzGRn63ALfmJE/" : "team22",
	"MsYVFSs1DqplCD648CLMN." : "team23",
	"2yMDuIEVLYaDgZMVZQRlW/" : "team24",
	"dQEzzoiAQyQ8gxdNhikz6." : "team25",
	"RRw4P00L5wn3.6VFLuhte/" : "team26",
	"smQ8Y1O7LfV3yG/5dWuvb/" : "team27",
	"X.75WJhn3pTrryOmEGcY3." : "team28",
	"r8UdRQzy6JvGGvA2B0HpZ." : "team29",
	"Csc6Kyx43efmL0sIdsin7." : "team30",
	"0T2.rotML2mLCHpiW6Oqz/" : "team31",
	"7Fi8kbvsbMsIZSw7MSRJ.." : "team32",
	"3FwUU3G.SADOSUOYO2Msc0" : "team33",
	"iULBOky8sTyOpIIhZJos5/" : "team34",
	"bHF3tftnEKtZsiG/jlmJn." : "team35",
	"fAsVMU7HimXiIW5zp1JzZ/" : "team36",
	"WV7YvTcWY43N8oVC4Gkob1" : "team37",
	"fyvB82NvBRPWh9cW8OgNU1" : "team38",
	"k/jP2N/zN3rcH99EPXC5l." : "team39",
	"WWkD4idIBJxT6tLe/mPUG1" : "team40",
	"krbYLQat9Ajoigi/FKt2x/" : "team41",
	"Hdc3R7F4uBNeV/VyjbI0V0" : "team42",
	"ibg358pQz/Bk0h34blkNW1" : "team43",
	"SiSI67AU8pqBHxtUDRWhB." : "team44",
	"1WN2TGXmFD6aH75NNcFZB." : "team45",
	"B96oRTlE0yZWjRx7qoO920" : "team46",
	"DbF6xvgpiK3Nu1un54h3V1" : "team47",
	"u6EkeePAlgl3wYcJ56O9o." : "team48",
	"OuCy/cfigw2ZVyQ0bkOOU." : "team49",
	"L1zWXhnkkBA9p8o.wdn511" : "team50",
	"CD3hivje3TwA1E32pTFas/" : "team51",
	"3ASc7BGkam3wN/aPdobGm/" : "team52",
	"YPWbj9DetbKYBwRLVRabe/" : "team53",
	"arFdI4oDuHPH/mF4z4BTx." : "team54",
	"dByOoI/B5RELArX/lmrmR." : "team55",
	"uUBgIJxiC2K8.F0/wkmzI." : "team56",
	"tpuKFlkkJBjcaWEQjim/J." : "team57",
	"W1l30eZxa8/BbVaBTmACj1" : "team58",
	"hQcquSV.RE3OPEzzEbPX5." : "team59",
	"AVjpgyHgol/UZ8PHX3Yj.0" : "team60",
}

solved = ["done"]
CryptBase = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
md5CryptSwaps = [12, 6, 0, 13, 7, 1, 14, 8, 2, 15, 9, 3, 5, 10, 4, 11]
salt = "hfT7jp2q"
magic = "$1$"

def ALTsum(inputStr):
	myHash = hashlib.md5()
	decodedInput = inputStr
	myHash.update((decodedInput + salt + decodedInput).encode("utf-8"))
	return myHash

def interSum(password,altSum,encodedPassword):
	intersum = password + magic + salt
	intersum = intersum.encode("utf-8")
	for i in range(len(password)):
		intersum += bytearray([altSum.digest()[i % 16]])
	myHash = hashlib.md5()
	myHash.update((intersum))
	
	pwSize = len(password)
	while (pwSize != 0):
		if pwSize&1 == 0:
			intersum += password[0].encode("utf-8")
		else:
			intersum += chr(0).encode("utf-8")
		pwSize >>= 1 
	myHash = hashlib.md5()
	myHash.update((intersum))
	return  myHash

def unsigned(n):
	return n & 0xFFFFFFFF

def fastHash(intermedite,password,salt):	
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
	#return magic +  salt+ '$' + returnStr
	return returnStr

def genHash(password):
	altsum = ALTsum(password)
	intersum = interSum(password,altsum,password)
	fasthash = fastHash(intersum,password,salt)
	reorderResult =  reorder(fasthash)
	return aryToStr(reorderResult)

# password generation
idxs = [ 0, 0, 0, 0, 0, 0, 0 ]
idx = 0
DICT_LENGTH = 26
MAX_PASS_LENGTH = 6
sDict = "abcdefghijklmnopqrstuvwxyz"

def getPassCombo():
	global idx
	global idxs 
	global sDict
    # clear buffer
	sPass = ""
    # end of the sequence
	if idx < MAX_PASS_LENGTH:
		# build string phase
		for i in range(0, idx+1):
			sPass += sDict[idxs[i]]

      	# advance phase
		idxs[0] = idxs[0] + 1
		for i in range(0, MAX_PASS_LENGTH):
			if idxs[i] == DICT_LENGTH:
				idxs[i] = 0
				if idx < i + 1:
				    idx = i + 1
				else:
				    idxs[i + 1] = idxs[i + 1] + 1
			else:
				break

	return sPass

testCounter = 0
globalLock = threading.Lock()

def getNewPasswordCombination():
	# protect getPassCombo() from data races with mutex
	global testCounter
	global globalLock
	globalLock.acquire()
	newPassword = getPassCombo()
	testCounter = testCounter + 1
	if testCounter > 0 and testCounter % 1000 == 1:
		seconds_since = time.time() - start_time
		print("Tested {0} K combinations, {1} / second".format( int(testCounter / 1000), int(testCounter/seconds_since)))
	globalLock.release()
	return newPassword

def consumer_thread(threadId):
	globalLock.acquire()
	print("Starting thread {0}".format(threadId))
	globalLock.release()

	global teamsDict
	while True:
		myPWD = getNewPasswordCombination()
		if myPWD == "":
			break
		pwdHash  = genHash(myPWD)
		if pwdHash in teamsDict:
			print(teamsDict[pwdHash] + " : " + myPWD)

def startThreading(numberOfThreads):
	print("Starting {0} threads ...".format(numberOfThreads))
	for i in range(0, numberOfThreads):
		threading.Thread(target=consumer_thread, args=(i,)).start()
				
def main():
	#while True:
	#	print(getPassCombo())
	# sanity test
	if "G3yf0NUx7mUkX.LIFWQxN." != genHash("password"):
		print("Sanity test failed")
		return 1
		
	cpus = os.cpu_count()
	startThreading(cpus)

start_time = time.time()
main()
#print("--- %s seconds ---" % (time.time() - start_time))
