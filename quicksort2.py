# 2. 1에서 생성된 CSV를 입력받아 Quick sort를 이용하여 정렬후 저장하고 이때 처리된 시간과 메모리 크기를 측정하여 표기하는 코드
import random
import csv
import time
import psutil

def partiton(arr,start,end):
    
    rdm = random.randint(start, end)    
    pivot = arr[rdm]    # pivot이 항상 편향되는 최악의 경우를 막기 위해 pivot 값을 매번 랜덤한 위치에서 선택

    while start <= end:
        while arr[start] < pivot : start += 1 # 시작 인덱스 값과 pivot 값을 비교해서 더 작으면 반복하여 시작 인덱스 값 증가
        while arr[end] > pivot : end -= 1 # 끝 인덱스 값과 pivot 값을 비교해서 더 작으면 반복하여 끝 인덱스 값 감소
        if start <= end :
            arr[start],arr[end] = arr[end],arr[start]   # 두 인덱스가 서로 교차하여 지나치지 않았다면 swap
            start += 1  # 인덱스 각자 진행 방향으로 한 칸씩 이동
            end -= 1    # 인덱스 각자 진행 방향으로 한 칸씩 이동
    return start #pivot보다 큰 그룹의 첫 번째 idx

def quicksort(arr,start,end):
    mid = partiton(arr,start,end) # 분할기준점
    if start < mid-1 : # 작은 그룹에 있는 값 개수가 1개가 될 때까지 quicksort 수행
        quicksort(arr,start,mid-1)
    if mid < end : # 큰 그룹에 있는 값 개수가 1개가 될 때까지 quicksort 수행
        quicksort(arr,mid,end)

def memory_use():
    p = psutil.Process()
    rss = p.memory_info().rss/2**20
    return rss

# 생성된 csv를 입력받아 quicksort를 이용하여 정렬 후 저장하고 이때 처리된 시간과 메모리 크기를 측정하여 출력하는 함수
def save_csv(name: str='csv_name'):
    arr= []
    with open(f'Sorted_{name}.csv', 'w', newline='') as wf:
        with open(f'{name}.csv', 'r') as rf:
            for line in rf:
                arr.append(int(line))
            start_memory = memory_use()
            start_time = time.time()
            quicksort(arr,0,len(arr)-1)
            end_time = time.time()
            end_memory = memory_use()
        for l in arr:
            wr = csv.writer(wf)
            wr.writerow([l])
    print(f"Sorted_{name} 처리 시간 : {end_time - start_time} 초 ")
    print(f"Sorted_{name} 메모리 사용량 : {end_memory - start_memory} MB")

if __name__ == '__main__':
    save_csv('Asend')
    save_csv('Desend')
    save_csv('Random')