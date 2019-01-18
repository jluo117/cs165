from passlib.hash import md5_crypt
h = md5_crypt.using(salt = "hfT7jp2q").hash("password")
print(h)