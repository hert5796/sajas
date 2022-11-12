from flask import Flask, render_template, request
from redactinator.v0 import redact as redactor


server = Flask(__name__)


@server.route('/')
def main():
    return render_template("index.html", redacted_text = "")

@server.route('/redact')
def redact():
    text = request.args.get("input")
    return render_template("index.html", redacted_text = redactor(text))

if __name__ == '__main__':
    server.run(debug = True)