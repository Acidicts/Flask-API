from flask import Flask, jsonify, Blueprint, request, redirect
from random import randint
# from llama_cpp import Llama

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

    switch = {
        'help': 'Sending Help!',
        'hello': "h12",
        'bye': 'Goodbye!'
    }
    oup = switch.get(inp, 'Invalid Code!')

    temp = 0

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


@requests.route('/')
def index():
    return redirect('/api')


@requests.route('/help')
def help():
    return redirect('/api?code=help')


@requests.route('/hello')
def hello():
    return redirect('/api?code=hello')


@requests.route('/bye')
def bye():
    return redirect('/api?code=bye')


# @requests.route('/ai')
# def ai():
#     model_path = ".. /API/llama-2-7b-chat.Q2_K.gguf"
#
#     prompt = request.args.get('prompt')
#     llm = Llama(model_path=model_path, n_ctx=2048)
#
#     # Generate a response
#     output = llm(prompt)
#
#     return output["choices"][0]["text"]
