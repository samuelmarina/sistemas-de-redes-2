from variables import msgs as M
from helpers import checkWrongAnswer
from tasks import getActInfo, findCriticalPath

tasks = dict()


def requestInput():
    act_num = input(M['msg1'] + '\n')
    act_num = checkWrongAnswer(act_num)
    getActInfo(act_num, tasks)


def start():
    requestInput()
    findCriticalPath(tasks)


start()
