from hashring import HashRing

def test_basic_ring():
    hr = HashRing(range(3))
    actual = hr.get_node('howdy')
    expected = 1
    assert expected == actual
