import sys
infile = "systm/dgjkhe82y/tmp/input2.txt"
sys.stdin = open (infile)
#----------------------------------
line = ""
whole =""
lines = 0
vowels = 0

while line!="end":
  whole = whole+(line+"\n")
  lines = lines+1
  vowels = vowels+(line.count("a")+line.count("e")+line.count("i")+line.count("o")+line.count("u")+line.count("A")+line.count("E")+line.count("I")+line.count("O")+line.count("U"))
  line = input().strip()
wordtable = whole.split()
words = len(wordtable)

lines=lines-1

print("Lines:",lines)
print("Words:",words)
print("Vowels: "+str(vowels))
print(whole.strip("\n"))