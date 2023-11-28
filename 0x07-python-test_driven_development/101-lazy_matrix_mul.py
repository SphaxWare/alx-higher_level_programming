#!/usr/bin/python3
"""
This module multiply 2 matrix with numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply 2 matrix
    Args:
        m_a: input first matrix
        m_b: input second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
