string = input()

num1 = int(string[0:3].strip())
num2 = int(string[3:6].strip())
num3 = int(string[6:9].strip())
num4 = int(string[9:12].strip())
num5 = int(string[12:])
good = 0
bad = 0
if num1 >=15:
  good = good+1
else:
  bad=bad+1
if num2 >=15:
  good = good+1
else:
  bad=bad+1
if num3 >=15:
  good = good+1
else:
  bad=bad+1
if num4 >=15:
  good = good+1
else:
  bad=bad+1
if num5 >=15:
  good = good+1
else:
  bad=bad+1
print("Good:",good)
print("Slow:",bad)