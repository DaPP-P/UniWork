import re

class testfile():

    def main():
        text = ['DOOR', 'SQUARE', 'CAT', 'DOGS', 'ANGLE', 'CANT']
        char = 'A'
        index = 1
        res = [idx for idx in text if idx[index] == char]
        print(res)

    if __name__ == "__main__":
        main()
