from flask import *
from pynput.mouse import Button, Controller

app = Flask("remoteMouse")
mouse = Controller()

@app.route("/rmb")
def rmb_c():
	mouse.click(Button.right)
	return "ok"

@app.route("/lmb")
def lmb_c():
	mouse.click(Button.left)
	return "ok"

@app.route("/rmb_h")
def rmb_h():
	mouse.press(Button.right)
	return "ok"

@app.route("/rmb_r")
def rmb_r():
	mouse.release(Button.right)
	return "ok"

@app.route("/lmb_h")
def lmb_h():
	mouse.press(Button.left)
	return "ok"

@app.route("/lmb_r")
def lmb_r():
	mouse.release(Button.left)
	return "ok"

@app.route("/")
def index():
	return render_template("index.html")

app.run(host="0.0.0.0", port=80)