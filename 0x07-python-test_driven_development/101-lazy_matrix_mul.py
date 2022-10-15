#!/usr/bin/python3
""" This module performs matrix multiplication using NumPy. """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Return the product of m_a and m_b. """
    return numpy.matmul(m_a, m_b)
