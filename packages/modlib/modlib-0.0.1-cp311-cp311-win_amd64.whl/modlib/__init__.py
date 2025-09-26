from modlib import fibonacci_cpp, fibonacci_cy
from .fibonacci_py import fibonacci_py

def fibonacci_cpp_from_py(a):
    return fibonacci_cpp.fibonacci_cpp(a)

def fibonacci_cy_from_py(a):
    return fibonacci_cy.fibonacci_cy(a)

