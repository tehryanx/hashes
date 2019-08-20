import hashlib, zlib, base64
import sys

if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
  print "USAGE: hashes [-b] string"
  print "-------------------------"
  print " -b will base64 encode the string before hashing it"
  print " -bu will do the same using the urlsafe charset"
  exit()
clear = "" # clear stores the cleartext string

# probably should use a cli argument library. oops.
string_pos = 2 if sys.argv[1] == '-b' or sys.argv[1] == '-bu' else 1

# parse cli for our string
for i in range(0, len(sys.argv)):
  if i>=string_pos:
    clear += " " + sys.argv[i]
clear = clear.strip()

# if b is set b64 encode the string
if sys.argv[1] == '-b':
        clear = base64.b64encode(clear)
elif sys.argv[1] == '-bu':
        clear = base64.urlsafe_b64encode(clear)

# loop through all digests available in hashlib
for i in hashlib.algorithms_available:
    tab = "\t\t" if len(i)<7 else "\t"
    h = hashlib.new(i)
    h.update(clear)
    print i, tab, h.hexdigest()

# adler32 and crc32 from zlib
print "crc32 signed", "\t", hex(zlib.crc32(clear))
# bitwise and with ffffffff to convert to unsigned int
print "crc32 unsigned", "\t", hex(zlib.crc32(clear) & 0xffffffff)
print "adler32 signed", "\t", hex(zlib.adler32(clear))
print "adler32 unsign", "\t", hex(zlib.adler32(clear) & 0xffffffff)

print "base32", "\t\t", base64.b32encode(clear)
print "base64", "\t\t", base64.b64encode(clear)
print "base64 urlsafe", "\t", base64.urlsafe_b64encode(clear)
