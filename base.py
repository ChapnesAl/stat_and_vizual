import statistics as st

data = [1, 2, 3, 4, 5]

'''Среднее значение'''


def my_mean(massive):
    return sum(massive) / len(massive)


r_av = st.mean(data)


''' Медиана '''



if __name__ == '__main__':
    print(r_av)
