import sys
infile = "systm/dgjkhe82y/tmp/input15.txt"
sys.stdin = open (infile)
#----------------------------------
o = int(input())
string = str(input())

if o==1:
  a = string[0].capitalize()
  print(a+string[1:])
if o==2:
  print(string.title())
if o==3:
  print(string.upper())
if o==4:
  print(string.lower())
if o==5:
  print(string.rjust(20))
if o==6:
  print(string.center(20)+"!")
if o==7:
  print("!".join(string))
if o==8:
  print(string.swapcase())