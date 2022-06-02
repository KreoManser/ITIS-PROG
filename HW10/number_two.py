"""
    - Здесь проверка линейного увелчиения скорости
    - Первая функция будет считаться долго(у меня на маке 37 секунд например)
    - Вторая функция будет считаться в разы быстрее(у меня 7-8 секунд)
"""

import time
import multiprocessing

def heavy(n):
    for x in range(1, n):
        for y in range(1, n):
            _ = x ** y

def heavy_proc(n):
    for x in range(1, n):
        for y in range(1, n):
            _ = x**y

def sequential(n):
    for i in range(n):
        heavy(500)

def sequential_proc(calc):
    for i in range(calc):
        heavy_proc(500)


def processesed(procs, calc):

    processes = []

    for process in range(procs):
        p = multiprocessing.Process(target=sequential_proc, args=(calc, ))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    start = time.time()
    sequential(80)
    end = time.time()
    print("Общее время работы однопотока: ", end - start)

    print("\n")

    start = time.time()
    # узнаем количество ядер у процессора
    n_proc = multiprocessing.cpu_count()
    print(f"Всего {n_proc} ядер в процессоре")
    calculate_cycle = 80 // n_proc + 1
    processesed(n_proc, calculate_cycle)
    end = time.time()
    print(f"На каждом ядре произведено {calculate_cycle} циклов вычислений")
    print(f"Итого {n_proc * calculate_cycle} циклов за: ", end - start)
