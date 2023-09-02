import time


# デコレータを用いて、過去に計算された結果をキャッシュする
def memorize(func):
    cache = {}

    def _wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return _wrapper



@memorize
def parts_sum(remained_sum, current_value):
    if remained_sum < current_value:
        return 0
    elif remained_sum < current_value * 2:
        return 1
    elif remained_sum < current_value * 3:
        return remained_sum // 2 - current_value + 2
    else:
        # return sum([parts_sum(remained_sum - current_value - i, current_value + i) for i in range(0, remained_sum // 2 + 1 - current_value)]) + 1
        return parts_sum(remained_sum - current_value, current_value) + parts_sum(remained_sum, current_value + 1)


def calc_decomposited_sum(num):
    return parts_sum(num, 1)


if __name__ == "__main__":
    time_start = time.time()
    for i in range(2, 1001):
        num1 = calc_decomposited_sum(i)
        # if i <= 20:
        #     print(f"{i:4}の和分解の組合せ数: {num1:50,}")
        # if i % 100 == 0:
        #     print(f"{i:4}の和分解の組合せ数: {num1:50,}")

    time_end = time.time()
    print(time_end - time_start)
