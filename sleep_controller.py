import os

from flask import Flask

app = Flask("FlaskApp")


@app.route("/sleep")
def sleep_func():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    return "Sleeping"


@app.route("/shutdown")
def shutdown_func():
    os.system("shutdown /s")
    return "Shutting down"


@app.route("/restart")
def restart_func():
    os.system("shutdown /r")
    return "Restarting"


def runApi(SERVER_HOST_IP, SERVER_HOST_PORT):
    from waitress import serve
    serve(app, host=SERVER_HOST_IP, port=SERVER_HOST_PORT)
