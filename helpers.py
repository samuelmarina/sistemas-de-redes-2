def promptWrongAnswer(msg):
    """ Pedir al usuario que reingrese su respuesta
    Returns:
        string obtenido del input
    """
    print(msg)
    answer = input()
    return answer


def checkWrongAnswer(answer, start, stop):
    """ Validar respuesta correcta en un rango
    Args:
        answer: string respuesta del input
        start: integer indicando el mínimo valor de la respuesta
        stop: integer indicando el máximo valor de la respuesta
    Returns:
        integer indicando el índice de la ciudad
    """
    try:
        answer = int(answer)
        while answer < start or answer > stop:
            res = promptWrongAnswer(
                'Respuesta inválida, por favor ingrese un número válido')
            answer = int(res)
        return answer
    except:
        res = promptWrongAnswer(
            'Respuesta inválida, por favor ingrese un número válido')
        return checkWrongAnswer(res, start, stop)


def checkWrongAnswer(answer):
    """ Validar que la respuesta sea un entero positivo
    Args:
        answer: string respuesta del input
        start: integer indicando el mínimo valor de la respuesta
        stop: integer indicando el máximo valor de la respuesta
    Returns:
        integer indicando el índice de la ciudad
    """
    try:
        answer = int(answer)
        while answer <= 0:
            res = promptWrongAnswer(
                'Respuesta inválida, por favor ingrese un número válido')
            answer = int(res)
        return answer
    except:
        res = promptWrongAnswer(
            'Respuesta inválida, por favor ingrese un número válido')
        return checkWrongAnswer(res)
