#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the ispc-programador2022/a5g3-a5g3 Project
#     https://github.com/ispc-programador2022/a5g3-a5g3
#
# Copyright (c) 2022,
# 
# - [Escobar, Tomás](https://github.com/tomasescobar24)
# - [Ferreira, Juan David.](https://github.com/juniors90)
# - [Feraboli, Germán Alejandro.](https://github.com/IAferaboli)
# - [Ferragutti, Silvia](https://github.com/ferrsil)
# - [Espada, Cecilia](https://github.com/ceciespada) 
# - [Fehr, Julieta](https://github.com/julietacfehr) 
# - [Fioranelli, Bruno](https://github.com/brufio)
#
# =============================================================================
# DOCS
# =============================================================================

"""a5g3

funcion que calcule la varianza del vector obtenido en genrnd.
"""

# =============================================================================
# IMPORTS
# =============================================================================

def varianza(vector: list) -> float:
    """Permite calcular la varianza del vector cualquira.

    Parameters
    ----------
    vector : list[int, float]
        Una lista cualquira de números enteros. Tambíen podían ser
        números racionales.

    Returns
    -------
    sigma_al_cuadrado : float
        La varianza del vector.

    Raises
    ------
    Exception
        Retornará la excepción correspondiente (esto se puede mejorar).

    Examples
    --------

    >>> # Escribimos una lista 'fija' para testear
    >>> vector = [2, 4, 3, 6, 7, 33, 75, 30]
    >>> varianza_de_lista_ramdom = varianza(vector=vector)
    >>> varianza_de_lista_ramdom
    566.0
    >>> # si usamos la función genrnd
    >>> from genrnd import genrnd
    >>> vector1 = genrnd()
    >>> varianza_de_lista_ramdom = varianza(vector=vector1)
    >>> # varianza_de_lista_ramdom contiene la varianza correspondiente
    >>> # a la lista vector1.

    """
    try:
        n = len(vector)
        promedio = sum(vector)/n
        promedio_al_cuadrado = promedio**2
        cuadrados = [ x**2 for x in vector]
        suma_de_cuadrados_sobre_n = sum(cuadrados)/n
        sigma_al_cuadrado = suma_de_cuadrados_sobre_n - promedio_al_cuadrado
        return sigma_al_cuadrado
    except Exception as ex:
        raise Exception(ex)
