#!/usr/bin/env python3

import hashlib, zlib, base64, binascii
import inspect
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("string", help="The string you'd like to see results for")
group = parser.add_mutually_exclusive_group()
group.add_argument("-b", "--b64", help="Base64 encode the string before hashing", action="store_true")
group.add_argument("-bu", "--urlsafeb64", help="Base64 encode the string using the urlsafe charset before hashing", action="store_true")
args = parser.parse_args()

clear = args.string # clear stores the cleartext string

# if b is set b64 encode the string
if args.b64:
        clear = base64.b64encode(clear)
elif args.urlsafeb64:
        clear = base64.urlsafe_b64encode(clear)

# loop through all digests available in hashlib
clear = clear.encode('utf-8')

for i in hashlib.algorithms_available:
    tab = "\t\t" if len(i)<7 else "\t"
    h = hashlib.new(i)
    h.update(clear)
    try:
        print (i, tab, h.hexdigest())
    except:
        print (i+" 16", tab, h.hexdigest(16))
        print (i+" 32", tab, h.hexdigest(32))
        print (i+" 64", tab, h.hexdigest(64))


# Hex stream
print("Hex stream", "\t", binascii.hexlify(clear))

# adler32 and crc32 from zlib
# bitwise and with ffffffff to convert to unsigned int
print ("crc32 signed", "\t", hex(zlib.crc32(clear)))
print ("crc32 unsigned", "\t", hex(zlib.crc32(clear) & 0xffffffff))
print ("adler32 signed", "\t", hex(zlib.adler32(clear)))
print ("adler32 unsign", "\t", hex(zlib.adler32(clear) & 0xffffffff))


print ("base32", "\t\t", base64.b32encode(clear))
print ("base64", "\t\t", base64.b64encode(clear))
print ("base64 urlsafe", "\t", base64.urlsafe_b64encode(clear))
