from variables import msgs as M
from helpers import checkWrongAnswer, checkWrongAnswerPredecesor, checkWrongAnswerDuracion

taskStr = 'task'


def getActInfo(actNum, tasks):
    """ Obtener la información de todas las actividades
    Args:
        actNum: integer del número de actividades
        tasks: diccionario para guardar las actividades
    """
    for ac in range(actNum):
        num = ac + 1
        print(M['msg2'] + str(num))
        act = str(input(M['msg3']))
        pred = str(input(M['msg4']))
        if pred != '':
            pred_ver = str(checkWrongAnswerPredecesor(pred, 1, actNum))
            pred = pred_ver
        dur = str(input(M['msg5']))
        if dur == '':
            dur_vacio = str(checkWrongAnswerDuracion(dur))
            dur_ver = str(checkWrongAnswer(dur_vacio))
            dur = dur_ver
        print('\n')
        addTask(num, act, pred, dur, tasks)


def addTask(id, act, pred, dur, tasks):
    """ Agregar una nueva actividad al diccionario
    Args:
        id: integer id de la actividad
        act: string descripción de la actividad
        pred: array conjunto de predecesores
        dur: integer duración de la actividad
        tasks: diccionario para guardar las actividades
    """
    actInfo = dict()
    actInfo['id'] = str(id)
    actInfo['name'] = act
    if pred != '':
        actInfo['pred'] = pred.split(',')
    else:
        actInfo['pred'] = ['-1']
    actInfo['dur'] = dur
    addDefault(actInfo)
    tasks[taskStr + str(id)] = actInfo


def addDefault(actInfo):
    """ Agregar valores predeterminados
    Args:
        actInfo: diccionario de la actividad
    """
    actInfo['ES'] = 0
    actInfo['EF'] = 0
    actInfo['LS'] = 0
    actInfo['LF'] = 0
    actInfo['float'] = 0
    actInfo['isCritical'] = False


def forwardPass(tasks):
    """ Algoritmo para el forward pass
    Args:
        tasks: diccionario para guardar las actividades
    """
    for task in tasks:
        if('-1' in tasks[task]['pred']):
            tasks[task]['ES'] = 0
            tasks[task]['EF'] = (tasks[task]['dur'])
        else:
            for k in tasks.keys():
                current = tasks[k]
                for pred in current['pred']:
                    if(pred != '-1' and len(current['pred']) == 1):
                        current['ES'] = int(tasks[taskStr + pred]['EF'])
                        current['EF'] = int(current['ES']) + \
                            int(current['dur'])
                    elif(pred != '-1'):
                        if(int(tasks[taskStr + pred]['EF']) > int(current['ES'])):
                            current['ES'] = int(
                                tasks[taskStr + pred]['EF'])
                            current['EF'] = int(
                                current['ES']) + int(current['dur'])


def backwardPass(reversedTasks, tasks):
    """ Algoritmo para el backwards pass
    Args:
        reversedTasks: lista con los keys de los tasks invertidos
        tasks: diccionario para guardar las actividades
    """
    for task in reversedTasks:
        current = tasks[task]
        if(reversedTasks.index(task) == 0):
            current['LF'] = current['EF']
            current['LS'] = current['ES']

        for pred in current['pred']:
            if(pred != '-1'):
                currPred = tasks[taskStr + str(pred)]
                if(currPred['LF'] == 0):
                    currPred['LF'] = int(current['LS'])
                    currPred['LS'] = int(currPred['LF']) - \
                        int(currPred['dur'])

                    currPred['float'] = int(
                        currPred['LF']) - int(currPred['EF'])

                elif(int(currPred['LF']) > int(current['LS'])):
                    currPred['LF'] = int(current['LS'])
                    currPred['LS'] = int(currPred['LF']) - \
                        int(currPred['dur'])
                    currPred['float'] = int(
                        currPred['LF']) - int(currPred['EF'])


def findCriticalPath(tasks):
    """ Algoritmo de la ruta crítica
    Args:
        tasks: diccionario para guardar las actividades
    """
    forwardPass(tasks)
    reversedTasks = list()
    for key in tasks.keys():
        reversedTasks.append(key)
    reversedTasks.reverse()
    backwardPass(reversedTasks, tasks)
    printData(tasks)


def printData(tasks):
    """ Imprimir matriz con resultados
    Args:
        tasks: diccionario para guardar las actividades
    """
    print('id\tname\tdur\tES\tEF\tLS\tLF\tfloat\tisCritical\tpred')
    for task in tasks:
        curr = tasks[task]
        if(curr['float'] == 0):
            curr['isCritical'] = True
        print(str(curr['id']) + '\t' + str(curr['name']) + '\t' + str(curr['dur']) + '\t' + str(curr['ES']) + '\t' + str(curr['EF']) + '\t' +
              str(curr['LS']) + '\t' + str(curr['LF']) + '\t' + str(curr['float']) + '\t' + str(curr['isCritical']) + '\t' + '\t' + str(curr['pred']) )
