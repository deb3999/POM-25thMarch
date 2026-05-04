import pytest
def test_method1():
    print("This is the method 1")

@pytest.mark.smoke
def test_method2():
    print("This is the method 2")
@pytest.mark.smoke 
def test_method3():
    print("This is the method 3")    