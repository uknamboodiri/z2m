from random import randint
import sys

print(sys)
start = sys.argv[1]
end = sys.argv[2]

jackpot_number = randint(int(start), int(end))
print(f'Random game to guess a number between {start} & {end}: ')

while True:
    try:
        print(jackpot_number)
        user_input = int(input('please enter a number: '))
        if user_input == jackpot_number:
            print(f'finally, you are a genius')
            break
    except ValueError:
        print('value error, please enter a number')
