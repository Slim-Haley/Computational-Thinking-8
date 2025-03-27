# beginning
baseball_points = 0
football_points = 0

# middle
answer = input("what do you like more A) math, or B) Science?")
if answer == "A":
    baseball_points += 1
elif answer == "B":
    football_points += 1

answer = input("what do you like more A) video games, or B) eating?")
if answer == "A":
    baseball_points += 1
elif answer == "B":
    football_points += 1    


answer = input("what do you like more A) swimming, or B) the skiing?")
if answer == "A":
   football_points += 1
elif answer == "B":
    baseball_points += 1    


answer = input("what do you like more A) the gym, or B) sports?")
if answer == "A":
   football_points += 1
elif answer == "B":
   baseball_points += 1  

answer = input("what do you like more A) burger, or B) sushi?")
if answer == "A":
    baseball_points += 1
elif answer == "B":
    football_points += 1 

# end
if baseball_points>football_points:
    print("you are a baseball player")

elif football_points>baseball_points:
    print ("you are a football player")