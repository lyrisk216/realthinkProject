#星座程序

#star星座类
class CLS_star(object):
    def __init__(self, name, month1, day1, month2, day2, likeList):
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
def get_star_index(month, day):
    for i in range(len(starList)):
        if starList[i].is_in(month, day):
            return i

starList = [ ]
st00 = CLS_star('白羊', 3, 21, 4, 19, [9, 2, 8])
starList.append(st00)
st01 = CLS_star('金牛', 4, 20, 5, 20, [4, 7, 8])
starList.append(st01)
st02 = CLS_star('双子', 5, 21, 6, 21, [7, 1, 10])
starList.append(st02)
st03 = CLS_star('巨蟹', 6, 22, 7, 22, [3, 7, 5])
starList.append(st03)
st04 = CLS_star('狮子', 7, 23, 8, 22, [2, 6, 8])
starList.append(st04)
st05 = CLS_star('处女', 8, 23, 9, 22, [10, 3, 11])
starList.append(st05)
st06 = CLS_star('天秤', 9, 23, 10, 23, [1, 7, 5])
starList.append(st06)
st07 = CLS_star('天蝎', 10, 24, 11, 22, [10, 4, 1])
starList.append(st07)
st08 = CLS_star('射手', 11, 23, 12, 21, [0, 5, 9])
starList.append(st08)
st09 = CLS_star('摩羯', 12, 22, 1, 19, [6, 9, 8])
starList.append(st09)
st10 = CLS_star('水瓶', 1, 20, 2, 18, [7, 8, 9])
starList.append(st10)
st11 = CLS_star('双鱼', 2, 19, 3, 20, [4, 0, 6])
starList.append(st11)
while True:
    month1, day1 = eval(input('请输入你的日月:'))
    star1Index = get_star_index(month1, day1)
    print('你的星座是' + starList[star1Index].name + '座')

    month2, day2 = eval(input('请输入对方的月日:'))
    star2Index = get_star_index(month2, day2)
    print('对方的星座是' + starList[star2Index].name + '座')

    if starList[star2Index].likeList[0] == star1Index:
        print('祂很想做你的小弟')
    elif starList[star2Index].likeList[1] == star1Index:
        print('祂喜欢你!')
    elif starList[star2Index].likeList[2] == star1Index:
        print('祂希望中午请你吃饭')
    else:
        print('祂不喜欢你')

        
    










    
