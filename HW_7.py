# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Чтобы записать байты можно использовать список с числами и функцию bytes


import random


def file_generator(extension: str, 
                   mi_name_len: int=6,
                     max_name_len: int=30, 
                     min_bytes_num: int=256,
                   max_bytes_num: int=4096, 
                   num_of_file: int=42):
    
    for _ in range(num_of_file):
        name = ""
        name_length = random.randint(mi_name_len, max_name_len)
        for j in range(name_length):
            name += chr(random.randint(70, 80))
        print(name)

        rand_byte_num = random.randint(min_bytes_num, max_bytes_num)
        data = bytes(rand_byte_num)

        with open(f'{name}.{extension}', 'ab') as f:
            f.write(data)


if __name__ == '__main__':
    print(file_generator("md", num_of_file=3))

