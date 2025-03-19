

def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area() :
    msg = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
    area = 3.14 * msg * msg

    print(f'반지름이{msg}인 원의 넓이는 = 3.14 x {msg}x {msg} = {area}')

get_circle_area()


      

