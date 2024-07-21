
import random
import time

print("welcome to game R P S !")
name = input("please enter your name :")
print("Helllo" + " " + name)
print("Are you ready ? \n wait a minute to start !")
print("-" * 50)
time.sleep(60)

user_rate, sys_rate = 0, 0

while user_rate != 3 or sys_rate != 3:
 user_choice = input("'r' for rock , 's' for scissors , 'p' for paper ! \n what is your choice ? ")
 choices = ['r', 's', 'p']
 sys_choice = random.choice(choices)
 if user_choice == 'r' and sys_choice == 'r':
  print(" user choice : rock \n system choice : rock")
  print(user_rate, sys_rate)
 elif user_choice == 'r' and sys_choice == 's':
  user_rate += 1
  print(" user choice : rock \n system choice : scissors")
  print(user_rate, sys_rate)
 elif user_choice == 'r' and sys_choice == 'p':
  sys_rate += 1
  print(" user choice : rock \n system choice : paper")
  print(user_rate, sys_rate)

 elif user_choice == 's' and sys_choice == 'r':
  sys_rate += 1
  print(" user choice : scissors \n system choice : rock")
  print(user_rate, sys_rate)
 elif user_choice == 's' and sys_choice == 's':
  print(" user choice : scissors \n system choice scissors : ")
  print(user_rate, sys_rate)
 elif user_choice == 's' and sys_choice == 'p':
  user_rate += 1
  print(" user choice : scissors \n system choice : paper")
  print(user_rate, sys_rate)

 elif user_choice == 'p' and sys_choice == 'r':
  user_rate += 1
  print(" user choice : paper \n system choice : rock")
  print(user_rate, sys_rate)
 elif user_choice == 'p' and sys_choice == 's':
  sys_rate += 1
  print(" user choice : paper \n system choice : scissors")
  print(user_rate, sys_rate)
 elif user_choice == 'p' and sys_choice == 'p':
  print(" user choice : paper \n system choice : paper")
  print(user_rate, sys_rate)
  break

 else:
  print("Invalid choice!")

if user_rate > sys_rate:
 print("Won!")
elif user_rate < sys_rate:
 print("Los!")
else:
 print("Equal!")