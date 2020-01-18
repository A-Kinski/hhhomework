import random

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    count = 0
    while count < N:
        yield random.randint(1, 100)
        count += 1

# написать генераторное выражение, которое делает то же самое
N = 10
gen_expr = (random.randint(1, 100) for i in range(N))

# if __name__ == '__main__':
#     # gen_fun = gen(10)
#     # for i in gen_fun:
#     #     print(i)
#
#     for i in gen_expr:
#         print(i)