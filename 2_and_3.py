import argparse
from re import sub, UNICODE

parser = argparse.ArgumentParser()
parser.add_argument('writer', help= 'запись строки в файл',
                    type=str, nargs='*')
parser.add_argument('-f', '--file', help='указание файла, в который нужно записать текст',
                    type=str, nargs='+') # nargs='+' делает так, что если аргумент не передан, выдаёт ошибку
args = parser.parse_args()
file_name = 'Task1_output.txt'

if args.file:
    file_name = ' '.join(args.file)

result_name = sub(r'[^\w\s.]', '', file_name.replace(' ', '_'), flags=UNICODE) 
# sub заменяет все символы на пустые кроме букв, цифр, точек и нижних подчеркиваний
# шаблон [^\w\s.], где ^ - отрицание(все, кроме); \w - буквы, цифры, _; \s - пробел, табуляция и т.д.; . - точка
# flags=UNICODE нужно для обработки текста на русском

if result_name[-4:] != '.txt':
    result_name = f'{result_name}.txt'

with open(result_name, 'a', encoding='UTF-8') as file:
    alpha = ' '.join(args.writer)
    if len(alpha)>0:
        file.write(f'{alpha}\n')
# Для правильного использования кода, в терминале нужно вписывать один из следующих вариантов:
# python 2_and_3.py <ваш текст> - текст будет записан в файл Task1_output.txt
# python 2_and_3.py <ваш текст> --file(или -f) <название файла> - текст будет записан в написанный файл,
# если этого файла нет - создаёт его и записывает текст. если название файла не будет написано, выведет ошибку.