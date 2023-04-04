# print("welcome to canara bank!")
# current_balance= 1000
# Atm_pin= 1234
# chances=3
# while chances!=0:
#     User_pin= int(input("please enter the four digit pin:"))
#     if User_pin!= Atm_pin:
#         chances=-1
#         print("Wrong pin number")
#         print(f"you have{chances} chances left")
#     else:
#         User_choice=input("B:Balance D:Deposit W:withdraw ")
#         if User_choice=="B":
#              print(f"your total balance is {current_balance}")
#         elif User_choice=="D":
#              deposit_user=int(input("Enter the amount that you would like to deposit"))
#              total_balance=deposit_user+current_balance 
#              print(f"your have totally deposited Rs.{deposit_user}")
#              print(f"your total balance is{total_balance}")
#         elif User_choice=="W":
#              Withdraw_amount=int(input("Enter the amount you want to withdraw"))
#              if Withdraw_amount>current_balance:
#                  print("You have insufficient balance,Try again!")
#              else:
#                  total_balance=current_balance-Withdraw_amount
#                  print(f"You have withdrawn Rs.{Withdraw_amount}")
#                  print(f"You have balance amount is Rs.{total_balance}")
#     exit=input("Would you like to exit?Yes/No")
#     if exit=="Yes":
#         print("Thank you for using canara bank")
#         break
#     else:
#         continue

x = int(input("Enter first number: "))

if x >= 0: 
    if x > 0:
        print((x)+  "is positive")
    else:
        print(f"{x} is zero, neither positive nor negative")
else:
    print(f"{x} is negative")