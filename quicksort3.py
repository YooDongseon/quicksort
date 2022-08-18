# 3. 2에서 작성한 Quick Sort 를 python에서 기본 제공하는 list.sort() 메서드 또는 내장함수 sorted() 와 비교하여 개선하는 '자신만의' idea를 추가 구현한 코드
import time
import psutil

def partiton(arr,start,end):
    pivot = arr[(start+end)//2] # 개선사항 : 리스트의 정 가운데 있는 값을 pivot 값으로 선택한다.
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
# 내가 구현한 quicksort와 list.sort(), sorted()의 처리 시간, 메모리 사용량 비교 함수
def sort_cmp(name: str='csv_name'):
    arr1, arr2, arr3 = [], [], []
    with open(f'{name}.csv', 'r') as rf:
        for line in rf:
            arr1.append(int(line))
            arr2.append(int(line))
            arr3.append(int(line))

        quicksort_start_memory = memory_use()
        quicksort_start_time = time.time()
        quicksort(arr1,0,len(arr1)-1)
        quicksort_end_time = time.time()
        quicksort_end_memory = memory_use()

        sorted_start_memory = memory_use()
        sorted_start_time = time.time()
        sorted(arr2)
        sorted_end_time = time.time()
        sorted_end_memory = memory_use()

        sort_start_memory = memory_use()
        sort_start_time = time.time()
        arr3.sort()
        sort_end_time = time.time()
        sort_end_memory = memory_use()

    print(f"{name} quicksort 처리 시간 : {quicksort_end_time - quicksort_start_time} 초 ")
    print(f"{name} quicksort 메모리 사용량 : {quicksort_end_memory - quicksort_start_memory} MB")

    print(f"{name} sorted() 처리 시간 : {sorted_end_time - sorted_start_time} 초 ")
    print(f"{name} sorted() 메모리 사용량 : {sorted_end_memory - sorted_start_memory} MB")

    print(f"{name} arr.sort() 처리 시간 : {sort_end_time - sort_start_time} 초 ")
    print(f"{name} arr.sort() 메모리 사용량 : {sort_end_memory - sort_start_memory} MB \n")

if __name__ == '__main__':
    sort_cmp('Asend')
    sort_cmp('Desend')
    sort_cmp('Random')