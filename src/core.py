from flask import Flask
import flask
import requests as req

app=Flask(__name__)
server_list={"5001":0,"5002":0}

def free_server():
    pointer=10000000000
    lowest_port=None
    for key in server_list.keys():
        load=server_list[key]
        if load<pointer:
            pointer=load
            lowest_port=key
    return lowest_port

@app.route("/get")
def get():
    url=flask.request.full_path
    port=free_server()
    server_list[port]+=1
    print(server_list)
    res=req.get("http://127.0.0.1:{}{}".format(port,url[:-1]))
    return res.content
    
@app.put("/free/<port>")
def free(port):
    server_list[port]=server_list[port]-1
    print(server_list)
    return "added"
    

if __name__ == "__main__":
    app.run(port=5000)