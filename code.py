import random
sub1 = input("enter your 1st subject :")
sub2 = input("enter your 2nd subject :")
sub3 = input("enter your 3ed subject :")
sub4 = input("enter your 4th subject :")
sub5 = input("enter your 5th subject :")

list = [ sub1 , sub2 , sub3 , sub4 , sub5 ]
selected = random.choice(list)
print("subject-")
print(selected) 