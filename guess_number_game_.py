# guess the number game !....abs



import random
num =random.randint(1,20)
guess=int(input("Enter the number must ist less than 21:"))
i=1

while num!=guess:
 i+=1
 if i==5:
        print("~The game is End~")
        print("Sorry the number is ", num)
        break
 if num>guess:
        print("Number is too less !...")
 else:
        print("Number is too high !...")
 
 
 guess=int(input("Enter again:"))
 if guess==num: 
  print("~ You won ~")
  print(" Your correct the number is",num)
  print(i)         
        


    
