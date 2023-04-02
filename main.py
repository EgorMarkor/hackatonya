from flask import Flask, request
import logging
import json

app = Flask(name)
logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=['POST'])
def main():
    logging.info(request.json)

    response = {
        'version': request.json['version'],
        'session': request.json['session'],
        'response': {
            'end_session': False
        }
    }

    rq = request.json
    if rq['session']['new']:
        response['response']['text'] = 'Приветствие'  # ПРИВЕТСТВИЕ НАПИСАТЬ

    return json.dumps(response)