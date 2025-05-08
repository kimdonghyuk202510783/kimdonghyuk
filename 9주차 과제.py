shopping_bag = {}  

while True:
    item = input('상품명? ')
    if item == '':
        break
    
    count = int(input('수량? '))
    
    
    if item in shopping_bag:
        shopping_bag[item] += count
    else:
        shopping_bag[item] = count

    print(f'장바구니에 {item} {count}개가 담겼습니다')


print('>>> 장바구니 보기:')
total_count = 0
for item, count in shopping_bag.items():
    print(f'{item} {count}개')
    total_count += count

print(f'총 담은 수량: {total_count}개')
