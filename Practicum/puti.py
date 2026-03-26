import sys

sum_path = 0
sum_path1 = 0

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    m1 = [ 5, 5 ]
    m2 = [ 1, 1, 1, 1, 1 ]
    m3 = [ 3, 100, 100, 100, 100 ]
    m4 = [ 1, 1, 1, 1, 1 ]
    m5 = [ 2, 2, 2, 2, 1 ]
    m6 = [ 1, 1, 1, 1, 1 ]
    print(m1)
    print(m2)
    print(m3)
    print(m4)
    print(m5)
    print(m6)

    tek_pos = m1[0]
     # 0 - вправо, 1 - вниз
    def precalc_path(a, b):
        global sum_path, sum_path1
        pre_deside_move = 0
        sum_path += a
        sum_path1 += b
        
        if sum_path < sum_path1:
            return 0
        else:
            return 1


    pre_deside_move = precalc_path(m1[1], m2[0])
    print('Вправо: ', sum_path, 'Вниз: ', sum_path1, 'Решение: ', pre_deside_move, 'вправо' if pre_deside_move == 0 else 'вниз')
    pre_deside_move = precalc_path(m2[1], m3[0])
    print('Вправо: ', sum_path, 'Вниз: ', sum_path1, 'Решение: ', pre_deside_move, 'вправо' if pre_deside_move == 0 else 'вниз')


    #take_move
    #move_right
    #move_down
    #calc_move
    
    
    sys.exit(1)



if __name__ == '__main__':
    main()
