# TODO Написать свою реализацию функции для подсчёта числа вхождения элементов в список
def my_count(l: list, item):
    k = 0
    for element in l:
        if element == item:
            k += 1
    return k

example = [1,'ab','c','ab','1',2 ]
ans = my_count(example, 'ab')
print(ans)
