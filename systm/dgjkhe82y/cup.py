# cup.py v210207.1
import sys
import os
import glob
currentdir=sys.argv[1]
tempdir=currentdir+"/tmp"

file_list = glob.glob(tempdir + "/*.py")
gf_file=currentdir+"/gf.py"
if gf_file in file_list:
  print ("Almost deleted gf.py")
else:
  for file in file_list:
    os.remove(file)

file_list = glob.glob(tempdir + "/*.txt")
for file in file_list:
  os.remove(file)

fileout=tempdir+"/output1.txt"
with open (fileout,"w") as outfile:
  outfile.write("Error with Output File")

fileout=currentdir+"/2.sh"
with open (fileout,"w") as outfile:
  outfile.write("echo Error")
