# 1. 100만개의 임의의 정수를 csv로 생성하는 코드 (랜덤 상태, 순방향 정렬 상태, 역방향 정렬 상태 생성)
import csv
import random

list = []
for i in range(1, 1000001):
    list.append(i)

# 순방향 정렬 상태 csv
with open('Asend.csv', 'w', newline='') as f :
    for l in list:
        wr = csv.writer(f)
        wr.writerow([l])

# 역방향 정렬 상태 csv
with open('Desend.csv', 'w', newline='') as f :
    for l in list[::-1]:
        wr = csv.writer(f)
        wr.writerow([l])   

random.shuffle(list)
# 랜덤 상태 csv
with open('Random.csv', 'w', newline='') as f:
    for l in list:
        wr = csv.writer(f)
        wr.writerow([l])