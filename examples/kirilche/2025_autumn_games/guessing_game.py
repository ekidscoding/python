from random import randint

# minimum, maximum = 1, 10
minimum = 7
maximum = 30

random_number = randint(minimum, maximum)
# print(f"Комп'ютер загадав {random_number}")
print(f'Введіть число між {minimum} та {maximum}.')

while True:
  # user_guess = int(input('Введіть число: '))
  raw_input = input('Введіть число: ')
  user_guess = int(raw_input)
  print(type(user_guess))
  # break
  if user_guess < random_number:
    print('Замало')

  if user_guess > random_number:
    print('Забагато')

  if user_guess == random_number:
    print('Ви вгадали число')
    break

print("Дякую за гру!")