package main

import (
	"fmt"
	"crypto/md5"
)

var md5CryptSwaps = [16]int{12, 6, 0, 13, 7, 1, 14, 8, 2, 15, 9, 3, 5, 10, 4, 11}

const itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

func main() {
	var pw = "password"
	var salt = "hfT7jp2q"
	var magic = "$1$"
	fmt.Printf("The hash for %s is %s", pw, string(MD5Crypt([]byte(pw), []byte(salt), []byte(magic))))
}

func MD5Crypt(password, salt, magic []byte) []byte {
    //Initialization
    intermediate := md5.New()
    alternate := md5.New()

    intermediate.Write(password)
    intermediate.Write(magic)
    intermediate.Write(salt)

    alternate.Write(password)
    alternate.Write(salt)
    alternate.Write(password)

    for i, mixin := 0, alternate.Sum(nil); i < len(password); i++ {
        intermediate.Write([]byte{mixin[i%16]})
    }

    for i := len(password); i != 0; i >>= 1 {
        if i&1 == 0 {
            intermediate.Write([]byte{password[0]})
        } else {
            intermediate.Write([]byte{0})
        }
    }
    fmt.Printf("%x", intermediate.Sum(nil))
    final := intermediate.Sum(nil)
    // Stetching
    for i := 0; i < 1000; i++ {
        hasher := md5.New()

        if i&1 == 0 {
            hasher.Write(final)
        } else {
            hasher.Write(password)
        }
        if i%3 != 0 {
            hasher.Write(salt)
        }
        if i%7 != 0 {
            hasher.Write(password)
        }
        if i&1 == 0 {
            hasher.Write(password)
        } else {
            hasher.Write(final)
        }
        final = hasher.Sum(nil)
    }

    //Finalization
    result := make([]byte, 0, 22)
    v := uint(0)
    bits := uint(0)
    for _, i := range md5CryptSwaps {
        v |= (uint(final[i]) << bits)
        for bits = bits + 8; bits > 6; bits -= 6 {
            result = append(result, itoa64[v&0x3f])
            v >>= 6
        }
    }

    return append(result, itoa64[v&0x3f])
}