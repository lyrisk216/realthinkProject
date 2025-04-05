#星座

#star星座类
class CLS_star(object):
    def __init__(self, name, month1, day1, month2, day2, likeList):#factory
        self.name = name
        self.month1 = month1
        self.day1 = day1
        self.month2 = month2
        self.day2 = day2
        self.likeList = likeList
    def is_in(self, month, day):
        if (month == self.month1) and (day >= self.day1):
            return True
        elif (month == self.month2) and (day <= self.day2):
            return True
        return False
#函数get_star_index()，输入月日，输出星座编号
def get_star_index(month, day):
    for i in range(len(starList)):
        if starList[i].is_in(month, day):
            return i#返回星座编号
        
#星座信息初始化
starList = [ ] #全局变量starList存放所有星座信息
st00 = CLS_star('白羊', 3, 21, 4, 19, [3, 8, 7])
starList.append(st00)
st01 = CLS_star('金牛', 4, 20, 5, 20, [4, 9, 8])
starList.append(st01)
st02 = CLS_star('双子', 5, 21, 6, 21, [11, 9, 2])
starList.append(st02)
st03 = CLS_star('巨蟹', 6, 22, 7, 22, [11, 7, 5])
starList.append(st03)
st04 = CLS_star('狮子', 7, 23, 8, 22, [9, 6, 8])
starList.append(st04)
st05 = CLS_star('处女', 8, 23, 9, 22, [10, 3, 11])
starList.append(st05)
st06 = CLS_star('天秤', 9, 23, 10, 23, [1, 4, 7])
starList.append(st06)
st07 = CLS_star('天蝎', 10, 24, 11, 22, [10, 6, 4])
starList.append(st07)
st08 = CLS_star('射手', 11, 23, 12, 21, [5, 10, 3])
starList.append(st08)
st09 = CLS_star('摩羯', 12, 22, 1, 19, [6, 9, 2])
starList.append(st09)
st10 = CLS_star('水瓶', 1, 20, 2, 18, [7, 8, 0])
starList.append(st10)
st11 = CLS_star('双鱼', 2, 19, 3, 20, [10, 2, 3])
starList.append(st11)

while True:
    month1, day1 = eval(input('请输入你的生日:'))
    star1Index = get_star_index(month1, day1)
    print('你的星座是' + starList[star1Index].name + '座')

    month2, day2 = eval(input('请输入对方的生日:'))
    star2Index = get_star_index(month2, day2)
    print('对方的星座是' + starList[star2Index].name + '座')

    if starList[star2Index].likeList[0] == star1Index:
        print('TA觉得你很抽象!')
    else:
        print('TA想对你说"呵呵"')
        
