def openBox():
    global count
    count -= 1
    print('상자를 열기')
    if (count == 0):
        print('선물')
        return
    openBox()
    print('상자 닫기')


count = 10
openBox()

