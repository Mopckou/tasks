import os
import time
import shutil


def get_expansion(s):
    index = s.find('.')
    return s[index:]


def move_file(path):
    abs_path, old_name = os.path.split(path)
    new_name = time.strftime('%d%m%y%H%S') + get_expansion(old_name)

    new_abs_path = os.path.join('./files_system', new_name)
    return shutil.move(path, new_abs_path)


if __name__ == '__main__':
    new_path = move_file('.\image\Figure_2.png')
    print(new_path)
    # после этого сохраняем в БД новый путь для удобного поиска в файловой системе
