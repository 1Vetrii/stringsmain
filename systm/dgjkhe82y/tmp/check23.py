import sys
infile = "systm/dgjkhe82y/tmp/input23.txt"
sys.stdin = open (infile)
#----------------------------------
option = int(input())
string = input()

if option == 1:
  c = len(string)
  for i in string:
    if c>-1:
      letter = string[c-1]
      print(letter)
      c=c-1
if option == 2:
  c = len(string)
  for i in string:
    if c>-1:
      letter = string[c-1]
      print(letter+"-")
      c=c-1
if option == 3:
  c = len(string)
  for i in string:
    if c>-1:
      letter = string[c-1]
      print(letter,end="")
      print("-",end="")
      c=c-1

if option==4:
  char = str(input())
  c = len(string)
  stop = c-10
  x = 0
  for i in string:
    if c>stop:
      letter = string[c-1]
      if letter == char:
        x = x+1
    c=c-1
  print(x)

if option==5:
  char = str(input())
  c = len(string)
  for i in string:
    if c>-1:
      letter = string[c-1]
      if letter == char:
        print("",end="")
      else:
        print(letter,end="")
    c=c-1

if option==6:
  c = len(string)
  x = 1
  done = False
  nth = int(input())
  for i in string:
    if c>-1:
      letter = string[c-1]
      if x%nth == 0 and done == False:
        print(letter,end="")
        c=c-1
        x = x+1
        done = True
      else:
        print("",end="")
        c=c-1
        x = x+1

if option==7:
  c = len(string)
  x = 1
  nth = int(input())
  for i in string:
    if c>-1:
      letter = string[c-1]
      if x>nth:
        print(letter,end="")
        c=c-1
        x = x+1
      else:
        print("",end="")
        c=c-1
        x = x+1

if option==8:
  c = len(string)
  x = 0
  nth = int(input())
  for i in string:
    if c>-1:
      letter = string[c-1]
      if x%nth == 0:
        print(letter,end="")
        c=c-1
        x = x+1
      else:
        print("",end="")
        c=c-1
        x = x+1