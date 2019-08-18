import hashlib
import sys

if len(sys.argv) < 2:
  print "USAGE: hashes string"

# pull string together
clear = ""
for i in range(0, len(sys.argv)):
  if i>0:
    clear += " " + sys.argv[i]

clear = clear.strip()

# loop through all available digests

for i in hashlib.algorithms_available:
    tab = "\t\t" if len(i)<7 else "\t"
    h = hashlib.new(i)
    h.update(clear)
    print i, tab, h.hexdigest()
