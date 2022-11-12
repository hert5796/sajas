from flask import Flask, render_template, request
from redactinator.v1 import redact as redactor
from json import loads


server = Flask(__name__)


@server.route('/')
def main():
    return render_template("index.html", original_text="", preserve_entities=set(), redacted_text="")


@server.route('/redact')
def redact():
    data = loads(request.args.get('data'))

    text = data['text']
    preserve_entities = set(data['preserve_entities'])

    redacted_text = redactor(text, preserve_entities)

    return render_template("index.html", original_text=text, preserve_entities=preserve_entities, redacted_text=redacted_text)


if __name__ == '__main__':
    server.run(debug=True)
