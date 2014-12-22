from hashring import HashRing

def test_basic_ring():
    hr = HashRing(range(3))
    actual = hr.get_node('howdy')
    expected = 1
    assert expected == actual


def test_server_ring():
    memcache_servers = ['192.168.0.246:11212',
                        '192.168.0.247:11212',
                        '192.168.0.249:11212']

    ring = HashRing(memcache_servers)
    actual = ring.get_node('my_key')
    expected = '192.168.0.247:11212'
    assert expected == actual
