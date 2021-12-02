from flask import Flask, redirect, url_for, request, render_template, session, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #json格式亂碼，改成ascii碼

@app.route("/", methods=['POST'])
def test():
	get_JsonInput = request.data.decode()
	b=get_JsonInput + "1111"
	return b


if __name__=="__main__":
    app.run(host='0.0.0.0', debug = False, port=5000, threaded=True)
