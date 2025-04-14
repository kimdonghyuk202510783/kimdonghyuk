
def read_single_digit(n) :
    if n == 1 :
        return '일'
    if n == 2 :
        return '이'
    if n == 3 :
        return '삼'
    if n == 4 :
        return '사'
    if n == 5 :
        return '오'
    if n == 6 :
        return '육'
    if n == 7 :
        return '칠'
    if n == 8 :
        return '팔'
    if n == 9 :
        return '구'
    if n == 0 :
        return '영'

def read_number() :
    num = int(input('세자리 정수 입력'))
    first_num = num // 100
    second_num = (num % 100) // 10
    third_num = num % 10

    print(read_single_digit(first_num), read_single_digit(second_num), read_single_digit(third_num))

read_number()
