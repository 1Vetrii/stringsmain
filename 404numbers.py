option = int(input())
numbers=input()
sum = int(numbers[0])+int(numbers[2])+int(numbers[4])+int(numbers[6])+int(numbers[8])
avg = sum/5

if option == 1:
  print(f"The sum of the numbers is {sum}")
elif option == 2:
  print(f"The average of the numbers is {avg:.1f}")