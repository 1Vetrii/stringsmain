sentence = str(input())

print(f"That sentence has {len(sentence)} characters")
print(f"The 3rd character is: {sentence[2]}")
print(f"The last character is: {sentence[-1]}")

if len(sentence) <20:
  print("It is a short sentence")
elif len(sentence) ==20:
  print("It is a perfect sentence")
elif len(sentence) >20:
  print("It is a long sentence")