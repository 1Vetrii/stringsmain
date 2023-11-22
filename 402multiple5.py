num = int(input())
mof = 0
mofs = 0
sum = 0
c = 0
while num != -99:
  if str(num)[-1] == "0" or str(num)[-1] == "5":
    mof = mof+1
    mofs = mofs+num
  c = c+1
  num = int(input())

print(f"You entered...\n{c} numbers\n{mof} of the numbers were multiples of 5\nThe sum of those numbers is {mofs}")