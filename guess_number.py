from random import randint


correct_number = randint(1,100)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Введите число: '))

    if guess < correct_number:
        print(f'Загаданное число больше чем {guess}')    
    elif guess > correct_number:
        print(f'Загаданное число меньше чем {guess}')
    elif guess == correct_number:
        print(f'Вы угадали! Число было {correct_number}')
        break