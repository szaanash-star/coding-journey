
# First Exercise

name = input("Before we begin, can i please know your name ?    :   ")
first_number = int(input(f"Now, {name}, could you please type a number ?    :   "))
second_number = int(input(f"Good. Now, can you give me another one {name} ? :   "))
if first_number > second_number:
    print(f"{first_number} is bigger than {second_number} !")
elif first_number == second_number:
    print(f"The numbers are equal {name} !")
else:
    print(f"{second_number} is bigger than {first_number} !")


# Second Exercise

third_number = int(input(f"Now, {name} , please give me another number, and i will tell you if the number is even or odd !  :   "))
if third_number % 2 == 0:
    print(f"{third_number} is an even number {name} ! ")
else:
    print(f"{third_number} is an odd number {name} ! ")


# Third Exercise

score = int(input(f"Now {name} please, give me a number from 0 to 100 ! :   "))
if score < 50:
    print(f"Well, i guess we will need to work on that, aren't we {name} ?")
else:
    print(f"Good job {name} ! It seems like you passed, hehe ! ")

# Forth Exercise

price = int(input(f"Now, {name}, could you please give me a price ? :   "))
discount = int(input(f"And what discount would you like for that price?     :   "))
final_price = price - (price * discount) / 100
print(f"Your final price will be {final_price} {name} !")