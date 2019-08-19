import hashlib, zlib, base64
import sys

if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
  print "USAGE: hashes [-b] string"
  print "-------------------------"
  print " -b will base64 encode the string before hashing it"
  exit()
clear = "" # clear stores the cleartext string

# probably should use a cli argument library. oops.
string_pos = 2 if sys.argv[1] == '-b' else 1

# parse cli for our string
for i in range(0, len(sys.argv)):
  if i>=string_pos:
    clear += " " + sys.argv[i]
clear = clear.strip()

# if b is set b64 encode the string
if sys.argv[1] == '-b':
        clear = base64.b64encode(clear)

# loop through all digests available in hashlib
for i in hashlib.algorithms_available:
    tab = "\t\t" if len(i)<7 else "\t"
    h = hashlib.new(i)
    h.update(clear)
    print i, tab, h.hexdigest()

# adler32 and crc32 from zlib
print "crc32", "\t\t", hex(zlib.crc32(clear))
print "adler32", "\t", hex(zlib.adler32(clear))

print "base64", "\t\t", base64.b64encode(clear)
