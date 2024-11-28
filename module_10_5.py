import multiprocessing
from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            str_line = file.readline()
            if str_line == '':
                break
            else:
                all_data.append(str_line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_timer = time.time()
    for i in filenames:
        read_info(i)
    end_timer = time.time()
    print(f'{end_timer - start_timer} (линейный)')

    start_timer = time.time()
    with Pool(4) as p:
        p.map(read_info, filenames)
    end_timer = time.time()
    print(f'{end_timer - start_timer} (многопроцессорный)')
