from passlib.hash import md5_crypt
import  time
start_time = time.time()
h = md5_crypt.using(salt = "hfT7jp2q").hash("password")
print("--- %s seconds ---" % (time.time() - start_time))
print(h)