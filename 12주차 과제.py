import os
import pickle

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n <= 0:
            break
        s.append(n)
        i += 1

    return s

def get_average(s):
    return sum(s) / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

filename = 'score.bin'

if os.path.exists(filename):
    print('[파일 읽기]')
    with open(filename, 'rb') as f:
        scores = pickle.load(f)
else:
    print('[점수 입력]')
    scores = input_scores()
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

print('\n[점수 출력]')
print('개인점수:', end=' ')
show_scores(scores)
print(f'평균: {get_average(scores):.1f}')


