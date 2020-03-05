# -*- Coding:utf-8 -*-

from random import random, randint


def setdoor():
    door = []
    for i in range(3):
        door.append(random())
    return door


def setchoice():
    chdoor = randint(0, 2)          # 随机选择门
    chswitch = randint(0, 1)        # 随机选择是否交换
    return chdoor, chswitch


def setswitch(chdoor, door):
    player = door[chdoor]
    for i in door:
        if player != i and i != min(door):
            return i


if __name__ == '__main__':
    times = int(input("Please input test times:"))
    total = times
    switchtimes = 0
    switchwin = 0
    staytimes = 0
    staywin = 0

    while times > 0:
        doorbase = setdoor()
        cd, cs = setchoice()
        if cs == 1:                          # cs返回0或1，1表示选择交换
            switchtimes += 1
            result = setswitch(cd, doorbase)
            if result == max(doorbase):
                switchwin += 1
                times -= 1
            else:
                times -= 1
        else:
            staytimes += 1
            if doorbase[cd] == max(doorbase):
                staywin += 1
                times -= 1
            else:
                times -= 1

    print("Total:{}".format(total))
    print("switch:{}".format(switchtimes))
    print("switch win:{:.3f}%".format(switchwin/switchtimes*100))
    print("stay:{}".format(staytimes))
    print("stay win:{:.3f}%".format(staywin/staytimes*100))
