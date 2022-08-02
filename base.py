import statistics as st

data = [1, 2, 3, 4, 5, 6]
data2 = [1, 2, 2, 3, 4, 5]
data3 = [1, 1, 2, 2, 3, 4, 5]
data4 = ['a', 'a', 'b', 'b', 'c', 'd', 'e']
data_outliers = [1, 2, 3, 4, 5, 6]


'''Среднее значение'''


def my_mean(massive):
    return sum(massive) / len(massive)


r_av = st.mean(data)

''' Медиана '''

r_med = st.median(data)

""" Мода и Мультимода """

r_mode = st.mode(data2)

r_mmode = st.multimode(data3)
r_mmode2 = st.multimode(data4)


if __name__ == '__main__':
    print(r_mmode)
    print(r_mmode2)
