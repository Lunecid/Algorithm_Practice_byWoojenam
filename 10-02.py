## 함수
def countDown(n):
    if n == 0:
        print('발사')
    else:
        print(n)
        countDown(n-1)

def printStar(n):
    if n > 0:
        printStar(n-1)
        print('별'*n)

printStar(5)


def gugu(dan, num):
    print(f'{dan} x {num} = {dan*num}')
    if num <9:
        gugu(dan, num+1)
        