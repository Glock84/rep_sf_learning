# Третья программа, компьютер сам загадывает и отгадывает число за минимальное количество попыток.

import numpy as np

def mean_predict(number:int = 1) -> int:
    """Угадываем число от среднего значения

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_num, max_num = 1, 100 # Устанавливаем границы загадываемого числа.
    
    while True:
        count += 1
        mean_num = ((min_num + max_num) // 2)
        if number < mean_num:
            max_num = mean_num
        elif number > mean_num:
            min_num = mean_num + 1
        else:
            #number == mean_num:
            break # выход из цикла
    return(count)

def score_game(mean_predict) -> int:
    """За какое кол-во попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        mean_predict (_type_): функция угадывания по среднему значению

    Returns:
        int: среднее кол-во попыток
    """
    
    count_ls = [] # список для сохранения кол-ва попыток
    np.random.seed(54) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000)) # загадали список из 1000 чисел
    
    for number in random_array:
        count_ls.append(mean_predict(number))
    
    score = int(np.mean(count_ls)) # находим среднее кол-во попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(mean_predict)