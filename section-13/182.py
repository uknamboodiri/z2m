try:
    with open("./app/sample.txt", mode='a') as sample_file:
        # sample_file.read()
        sample_file.write('how are you doing?')
        # sample_file.readline()

except FileNotFoundError as err:
    print("File not found error")
    raise err
except IOError as err:
    print("unable to read file")
    raise err
