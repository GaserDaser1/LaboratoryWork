import math
import time
import tracemalloc

def find_min_n(A, B):
    # Разложение A на простые множители
    def factorize(x):
        factors = {}
        while x % 2 == 0:
            factors[2] = factors.get(2, 0) + 1
            x = x // 2
        i = 3
        max_factor = math.sqrt(x) + 1
        while i <= max_factor:
            while x % i == 0:
                factors[i] = factors.get(i, 0) + 1
                x = x // i
                max_factor = math.sqrt(x) + 1
            i += 2
        if x > 1:
            factors[x] = factors.get(x, 0) + 1
        return factors
    
    factors_A = factorize(A)
    factors_B = factorize(B)
    
    # Проверка всех ростых множителей A есть в B
    for p in factors_A:
        if p not in factors_B:
            return -1


    # Вычисление минимального n
    n = 0
    for p in factors_A:
        required = (factors_A[p] + factors_B[p] - 1) // factors_B[p]  
        if required > n:
            n = required
    
    return n

def counter():
    tracemalloc.start()  # Начинаем отслеживание памяти
    start_time = time.time()  # Засекаем время начала

    print("Задание выполнил: Фурсов Вадим Сергеевич, группа 090301-ПОВа-о24")
    # Введите числа 
    A = 54
    B = 60
    result = find_min_n(A, B)
    print(result)
   

    elapsed_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Время выполнения: {elapsed_time:.6f} секунд")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")
if __name__ == "__main__":
    counter()