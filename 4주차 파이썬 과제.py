def get_fixed_price(dc , discount_price ) :
    original_price = discount_price // ((100 - dc) / 100)
    return original_price
    

dc = int(input("할인율은? ")) 
a = int(input('A상품의 할인된 가격은?'))
b = int(input('B상품의 할인된 가격은?'))

a_original_price = get_fixed_price(dc, a)
b_original_price = get_fixed_price(dc, b)

print('A 상품의 정가는', a_original_price , '원')
print('B 상품의 정가는', b_original_price, '원')
