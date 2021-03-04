print("What is your name human?")
n = input()
#print("Do you have a dog? (types True or False)")
#dog =  input()



if len(n) > 9:
  print ("You have very looong name!")
  print ("Your name contains {} letters".format(len(n)))
elif len(n) > 6:
 print("Yor name is a bit long. Consider a nickname") 
elif len(n) < 3: 
 print("Your name is not too long. Is it? :P ")
else: 
  print ("Your name is just normal lol")


