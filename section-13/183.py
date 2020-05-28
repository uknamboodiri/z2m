# translate a file to japanese
from translate import Translator

try:
    with open("./sample.txt", mode="r") as input_file:
        translator = Translator(to_lang="ja")
        while True:
            line = input_file.readline()
            translated_line = translator.translate(line)
            with open("./sample-ja.txt", mode="a") as output_file:
                output_file.write(translated_line)
            print(f"line {line}")
            if len(line) < 1:
                break
except FileNotFoundError as err:
    print("Please check file path")
    raise err
except IOError as err:
    print("IO File error")
    raise err
