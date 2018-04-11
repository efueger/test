from app import add, minus

def test_add():
    assert add(1,2)==3
    assert add(4,2)==6

def test_minus():
    assert minus(4,2)==2
    assert minus(7,2)==5

