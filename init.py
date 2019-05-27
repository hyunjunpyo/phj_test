
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello Hyunjun"

if __name__ == "__main__":
	app.run(host="192.168.0.196", port="8888")


