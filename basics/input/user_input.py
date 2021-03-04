print("What is your name human?")
name = input()
print(type(name))

n = input()


if len(n) > 9:
  print ("You have very looong name!")
  print ("Your name contains {} letters".format(len(n)))
else:
  print ("Your name is just normal lol")

  
print ("What is your age?")
age = int(input())
print (type(age))
print ("What is your bank balance?")
balance = float(input())
print ("Welcome {}. You are said to be {} years old. Your bank balance is {}.".format(name, age, balance ))