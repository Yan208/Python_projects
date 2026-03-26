import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    #numbers = '1000 -1000 0'
    #numbers = '3 1 3'
    #numbers = '1 2 3'
    numbers = input()
    count = 0
    
    num_spl = numbers.split(' ')

    for i in enumerate(num_spl):
        for j in enumerate(num_spl):
            for k in enumerate(num_spl):
                #print(int(i[1]), int(j[1]), int(k[1]))
                if int(i[1]) < int(j[1]) < int(k[1]) and not i == j and not j == k and not i == k:
                    print(j[1])
                elif int(i[1]) <= int(j[1]) <= int(k[1]) and not i == j and not j == k and not i == k: # нужно проверить чтобы число не сравнивалось само с собой
                    #print(j[1])
                    count += 1
                    if count <= 1:
                        #print('else ')
                        print(j[1])
    sys.exit(1)


if __name__ == '__main__':
    main()
