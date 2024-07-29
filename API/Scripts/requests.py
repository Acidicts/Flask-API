from flask import Flask, jsonify, Blueprint, request, redirect
from random import randint

requests = Blueprint('api', __name__)
ntl = {
    0: 'z',  # Added mapping for 0
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
}


@requests.route('/api', methods=['GET', 'POST'])
def api():
    inp = request.args.get('code')

    if request.method == 'GET':
        return jsonify({'message': 'Hello World!'})
    else:
        switch = {
            'help': 'Sending Help!',
            'hello': "h12",
            'bye': 'Goodbye!'
        }
        oup = switch.get(inp, 'Invalid Code!')

        if oup == 'h12':
            for i in range(randint(1, 50)):
                temp = str(randint(123456789, 987654321))
            new = []
            for length in range(len(temp)):
                new.append(ntl[int(temp[length])])

            temp = ''
            for l in new:
                temp = str(temp + l)

            return temp

        return jsonify({'message': str(oup)})
