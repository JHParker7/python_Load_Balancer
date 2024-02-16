import requests as req
import multiprocessing as par

def get(x):
    return req.get(url="http://127.0.0.1:5000/get").content.decode()

def load_balancer_stress(stress,threads):
    Pool=par.Pool(threads)
    stress=[None for x in range(stress)]
    res=Pool.map(get,stress)
    del Pool
    return res

def test_load_balancer_work():
    res=req.get(url="http://127.0.0.1:5000/get").content
    assert  res.decode() == "hello world"
    
def test_load_balancer_stress_2():
    stress=2
    assert load_balancer_stress(stress,2) == ["hello world" for x in range(stress)]
    
def test_load_balancer_stress_4():
    stress=4
    assert load_balancer_stress(stress,4) == ["hello world" for x in range(stress)]

def test_load_balancer_stress_10():
    stress=10
    assert load_balancer_stress(stress,4) == ["hello world" for x in range(stress)]
    
def test_load_balancer_stress_100():
    stress=100
    assert load_balancer_stress(stress,8) == ["hello world" for x in range(stress)]
    

