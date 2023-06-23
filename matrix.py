"""Módulo com as funções de manipulação de matrizes."""
from math import sqrt


def soma(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Soma duas matrizes"""
    if len(x) != len(y) or len(x[0]) != len(y[0]):
        return None

    result = []
    for i in range(len(x)):
        row = []
        for j in range(len(x[0])):
            row.append(x[i][j] + y[i][j])
        result.append(row)

    return result


def multiplicação_por_escalar(matriz: list[list[float]], escalar: float) -> list[list[float]]:
    """Multiplica uma matriz por um escalar"""
    result = []
    for i in range(len(matriz)):
        row = []
        for j in range(len(matriz[i])):
            row.append(matriz[i][j] * escalar)
        result.append(row)

    return result

def multiplicação(x: list[list[float]], y: list[list[float]]) -> list[list[float]] | None:
    """Multiplica duas matrizes"""
    if len(x[0]) != len(y):
        return None

    result = []
    for i in range(len(x)):
        row = []
        for j in range(len(y[0])):
            element = 0
            for k in range(len(y)):
                element += x[i][k] * y[k][j]
            row.append(element)
        result.append(row)

    return result

def norma(x: list[list[float]]) -> float:
    """Calcula a norma de uma matriz"""
    if not x:
        return 0

    norm_squared = sum(sum(elem**2 for elem in row) for row in x)
    norm = sqrt(norm_squared)

    return norm

def é_simétrica(x: list[list[float]]) -> bool:
    """Verifica se uma matriz é simétrica"""
    if len(x) != len(x[0]):
        return False

    transposed = transposta(x)

    return x == transposed

def transposta(x: list[list[float]]) -> list[list[float]]:
    """Calcula a transposta de uma matriz"""
    transposed = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

    return transposed
