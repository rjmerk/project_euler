'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
from utils import measure_execution_time


def main():
    print('Problem 22')
    with measure_execution_time():
        with open('../resources/p022_names.txt', 'r', encoding='ascii') as file:
            name_list = file.readline().replace('"', '').split(',')
        result = sum(name_scores(name_list))
    print(f'The total of all name scores in the file is {result}')


def name_scores(name_list):
    name_list.sort()
    for i, name in enumerate(name_list):
        name_score = sum(ord(char) - ord('A') + 1 for char in name)
        yield (i + 1) * name_score


if __name__ == '__main__':
    main()
