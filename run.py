print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

direction = input("Would you take left or right?\n").lower()
if direction == "left":
    action = input("Would you swim or wait? Swim or Wait?\n").lower()
    if action == "wait":
        door = input("Which door would you choose? Red, Yellow or Blue?\n").lower()
        if door == "red":
            print("You are burnt by fire. Game over!")
        elif door == "blue":
            print("You are eaten by beasts. Game over!")
        elif door == "yellow":
            print("You won!")
        else:
            print("You chose a door that does not exist. Game over!")            
    else:
        print("You are attacked by a trout. Game over!")
else:
    print("You fell into a hole. Game over!")

                    
