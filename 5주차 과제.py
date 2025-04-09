def rep_chair(c, n):
    print(c * n)

def draw_line_string():
    msg1 = input('input his/her name:')
    msg2 = 'Welcome to Seoul'

    nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)
    rep_chair('-', nstr)
    print(f'  {msg1}   ')
    print(msg2)
    rep_chair('-', nstr)

draw_line_string()

  
