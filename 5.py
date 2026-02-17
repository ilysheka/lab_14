import argparse
from re import sub, UNICODE

parser = argparse.ArgumentParser()
parser.add_argument('writer', help= 'запись строки в файл',
                    type=str, nargs='*')
parser.add_argument('-f', '--file', help='указание файла, в который нужно записать текст или вывести содержимое',
                    type=str, nargs='+')
parser.add_argument('-r', '--read', help='вывод содержимого указанного файла',
                    action='store_true')
parser.add_argument('-c', '--count', help='подсчёт количества строк в файле и количество слов',
                    action='store_true')
args = parser.parse_args()
file_name = 'Task1_output.txt'

if args.file:
    file_name = ' '.join(args.file)
    file_name = sub(r'[^\w\s.]', '', file_name.replace(' ', '_'), flags=UNICODE)
    if file_name[-4:] != '.txt':
        file_name = f'{file_name}.txt'

with open(file_name, 'a', encoding='UTF-8') as file:
    alpha = ' '.join(args.writer)
    if len(alpha)>0:
        file.write(f'{alpha}\n')

if args.read:
    with open(file_name, 'r', encoding='UTF-8') as file:
        for i in file.readlines():
            print(i, end='')

if args.count:
    with open(file_name, 'r', encoding='UTF-8') as file:
        file_readlines = file.readlines()
        count_lines = len(file_readlines)
        words = []
        for i in file_readlines:
            for n in i.split(' '):
                words.append(n)
        count_words = len(words)
        # print(file_readlines) - если нужна проверка
        # print(words)
    print(f'Количество строк в файле: {count_lines}\nКоличество слов в файле: {count_words}')