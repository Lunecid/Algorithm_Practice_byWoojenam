## 함수
import random

def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)
    mid = start + end / 2
    while (start <= end):
        if (ary[mid] == fData):
            pos = mid
            break
        elif (ary[mid] > fData):
            end = mid - 1
        else:
            start = mid + 1

    return pos

    return pos
## 변수
dataAry = [random.randint(30,190) for _ in range(8)]
findData = random.choice(dataAry)


## 메인
print('배열-->', dataAry)
position = binSearch(dataAry, findData)
if (position == -1):
    print(findData, '없어요 ㅠ')

print (findData,'는', position,'위치에 있어요')