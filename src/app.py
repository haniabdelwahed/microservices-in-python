from pprint import pp
from urllib import response
from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World FROM FALSK Api other port</p>"

@app.route("/appcheck")
def app_check():
    response_json = {"header": {"status":200, "app_name":"microservices-in-python"}, 
                "body":{"status":200, "status_message":"application is running"}}
    return jsonify(response=response_json)

def get_host_details():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/details")
def details():
    host_name, host_ip = get_host_details()
    return render_template("index.html", host_name=host_name, host_ip=host_ip)

if __name__ == '__main__':
    app.run(host="0.0.0.0"#, port=5001
            )

