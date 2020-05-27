while True:
    try:
        age = int(input('what is your age? '))
        10 / age
    except ZeroDivisionError:
        print('please enter number > 0')
    except ValueError:
        print('please enter a number')
    except (ArithmeticError, AttributeError) as err:
        print(f'Ooops {err} ')
    else:
        print('thank you')
        break
    finally:
        print('finally, I am done')
    print('can you hear me')