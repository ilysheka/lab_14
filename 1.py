import argparse

parser = argparse.ArgumentParser()
parser.add_argument('writer', help = 'запись строки в файл',
                    type=str, nargs='*') 
# nargs='*' - принимает все слова как список
# разница между nargs='*' и nargs='+' в том, что первый принимает 0 или более аргументов(если 0, пустой список),
# а второй принимает 1 и более аргументов, при 0 выдаёт ошибку
args = parser.parse_args()

with open('Task1_output.txt', 'a', encoding='UTF-8') as file:
    alpha = ' '.join(args.writer)
    if len(alpha)>0:
        file.write(f'{alpha}\n')
# Для работы программы, в терминал нужно написать: python first.py <любой текст>
# То, что вы напишете вместо <любой текст>, будет занесено в файл Task1_output.txt
# Этот файл находится в той же папке, что и файл с программой
