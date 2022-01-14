import random

print("------------------------------------------------------------")
print("Coin or Dice roller")
print("Made By 20730661")
print("------------------------------------------------------------")

print("dice or coin?")
dc_input= input(">>")

if dc_input== "coin":
    flip_coin = input("Write 'start' to flip the coin: ")

    if flip_coin == "start":
       posiblle_results_coin = [1,2]

       result_coin = random.choice(posiblle_results_coin)
       if result_coin== 1:
           print("...")
           print("The result of the coin toss is:")
           print("Heads")
           print("------------------------------------------------------------")
       else:
           print("...")
           print("The result of the coin toss is:")
           print("Tails")
           print("------------------------------------------------------------")

           #print("Result of coin flip is : " + str(result_coin))




else:
    if dc_input == "dice":
        roll_dice = input("Write 'start' to dice roll: ")

        if roll_dice == "start":
           posiblle_results_dice = [1, 2, 3, 4, 5, 6]
           result_dice = random.choice(posiblle_results_dice)
           print("Result of dice rolling is : " + str(result_dice))

           posiblle_results_dice = [1, 2, 3, 4, 5, 6]
           result_dice = random.choice(posiblle_results_dice)
           print("Result of dice rolling is : " + str(result_dice))

    else:
        if dc_input != "coin" or dc_input != "dice":
            print("invalid input. Please try again.")
            print("------------------------------------------------------------")
