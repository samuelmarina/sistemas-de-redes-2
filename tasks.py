from variables import msgs as M


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
        dur = str(input(M['msg5']))
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
        actInfo['pred'] = '-1'
    actInfo['dur'] = dur
    addDefault(actInfo)
    tasks['task' + str(id)] = actInfo


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
