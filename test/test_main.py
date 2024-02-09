import requests as req

def load_balancer_stress(stress):
    res=[req.get(url="http://127.0.0.1:5000/get").content.decode() for x in range(stress)]
    return res

def test_load_balancer_work():
    res=req.get(url="http://127.0.0.1:5000/get").content
    assert  res.decode() == "hello world"
    
def test_load_balancer_stress_2():
    stress=2
    assert load_balancer_stress(stress) == ["hello world" for x in range(stress)]
    
def test_load_balancer_stress_4():
    stress=4
    assert load_balancer_stress(stress) == ["hello world" for x in range(stress)]

def test_load_balancer_stress_10():
    stress=10
    assert load_balancer_stress(stress) == ["hello world" for x in range(stress)]
