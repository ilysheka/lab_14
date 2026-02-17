import argparse
from re import sub, UNICODE

parser = argparse.ArgumentParser()
parser.add_argument('writer', help= 'запись строки в файл',
                    type=str, nargs='*')
parser.add_argument('-f', '--file', help='указание файла, в который нужно записать текст или вывести содержимое',
                    type=str, nargs='+')
parser.add_argument('-r', '--read', help='вывод содержимого указанного файла',
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

# Для корректного использования кода, в терминале нужно писать следующее:
# python 4.py <ваш текст> - текст будет записан в файл Task1_output.txt
# python 4.py <ваш текст> --file(или -f) <название файла> - текст будет записан в написанный файл
# если этого файла нет - создаёт его и записывает текст. если название файла не будет написано, выведет ошибку.
# python 4.py <любой из шаблонов выше> --read(или -r) - сначала совершит то, что написано выше, и после выведет
# содержимого файла, переданного в --file; если не указан, выведет содержимое файла Task1_output.txt
# также можно использовать python 4.py --read - выведет содержимое файла Task1_output.txt