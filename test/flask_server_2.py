from flask import Flask
import requests as req
import logging

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
port = 5002

@app.get("/get")
def fake_get():
    req.put("http://127.0.0.1:5000/free/{}".format(port))
    return "hello world"

if __name__ == "__main__":
    app.run(port=port)