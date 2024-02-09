from flask import Flask
import flask
import requests as req

app=Flask(__name__)
server_list=[5001,5002]

@app.route("/get")
def get():
    url=flask.request.full_path
    free_server=server_list.pop(0)
    print(url)
    res=req.get("http://127.0.0.1:{}{}".format(free_server,url[:-1]))
    return res.content
    
@app.put("/free/<port>")
def free(port):
    server_list.append(port)
    return "added"
    

if __name__ == "__main__":
    app.run(port=5000)