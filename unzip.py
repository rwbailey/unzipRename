#Python 2.x

import zipfile

print "[*] Beginning extraction..."

zip = zipfile.ZipFile('data.zip')
for i, f in enumerate(zip.filelist):
  f.filename = 'extracted_{0:03}'.format(i)
  zip.extract(f)
  print "--- Extracted '%s'" % (f.filename)

print "[*] Done"


