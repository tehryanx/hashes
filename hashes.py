import hashlib, zlib
import sys

if len(sys.argv) < 2:
  print "USAGE: hashes string"

# pull string together
clear = ""
for i in range(0, len(sys.argv)):
  if i>0:
    clear += " " + sys.argv[i]

clear = clear.strip()

# loop through all digests available in hashlib

for i in hashlib.algorithms_available:
    tab = "\t\t" if len(i)<7 else "\t"
    h = hashlib.new(i)
    h.update(clear)
    print i, tab, h.hexdigest()

# adler32 and crc32 from zlib
print "crc32", "\t\t", hex(zlib.crc32(clear))
print "adler32", "\t", hex(zlib.adler32(clear))
