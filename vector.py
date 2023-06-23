"""Módulo com as funções de manipulação de vetores."""
from typing import List, Union
from math import sqrt

def norma(x: list[float]) -> float | None:
    """Calcula a norma de um vetor"""
    if not x:
        return None

    norm_squared = sum(elem**2 for elem in x)
    norm = sqrt(norm_squared)

    return norm


def soma(x: list[float], y: list[float]) -> list[float] | None:
    """Soma dois vetores"""
    if len(x) != len(y):
        return None

    result = [x[i] + y[i] for i in range(len(x))]
    return result


def multiplicação_por_escalar(vetor: list[float], escalar: float) -> list[float]:
    """Multiplica um vetor por um escalar"""
    result = [elem * escalar for elem in vetor]
    return result


def produto_interno(x: list[float], y: list[float]) -> float | None:
    """Calcula o produto interno de dois vetores"""
    if len(x) != len(y):
        return None

    result = sum(x[i] * y[i] for i in range(len(x)))
    return result


def produto_vetorial(x: list[float], y: list[float]) -> list[float] | None:
    """Calcula o produto vetorial de dois vetores"""
    if len(x) != 3 or len(y) != 3:
        return None

    result = [
        x[1] * y[2] - x[2] * y[1],
        x[2] * y[0] - x[0] * y[2],
        x[0] * y[1] - x[1] * y[0]
    ]
    return result



def produto_diádico(x: list[float], y: list[float]) -> list[list[float]] | None:
    """Calcula o produto diádico de dois vetores"""
    if len(x) != len(y):
        return None

    result = [[x[i] * y[j] for j in range(len(y))] for i in range(len(x))]
    return result
