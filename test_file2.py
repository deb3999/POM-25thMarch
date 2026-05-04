import pytest


def test_file2method1():
    print("This is the file2 method1")
@pytest.mark.smoke    
def test_file2method2():
    print("This is the file2 method2")
def test_file2method3():
    print("This is the file2 method3")    