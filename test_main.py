import pytest
from main import sum, resta , mult , div

def test_sum1():
    assert sum(2,5)== 7
    print("La funcion sum trabaja correctamente")
    
def test_sum2():
    assert sum(-2,-5)== -7
    print("La funcion sum trabaja correctamente")
    
def test_resta1():
    assert resta(2,5)== -3
    print("La funcion resta trabaja correctamente")
    
def test_resta2():
    assert resta(-2,-5)== 3
    print("La funcion resta trabaja correctamente")
    
def test_mul1():
    assert mult(2,5)== 10
    print("La funcion mult trabaja correctamente")
    
def test_mul2():
    assert mult(-2,-5)== 10
    print("La funcion mult trabaja correctamente")
    
def test_div1():
    assert div(-8,-4)== 2
    print("La funcion div trabaja correctamente")
    
def test_div2():
    assert div(1 , 1)== 1
    print("La funcion div trabaja correctamente")