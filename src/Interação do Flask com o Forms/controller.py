from flask import Flask, request

aplicacao = Flask(__name__)

@aplicacao.route('/delta', methods=['POST', 'GET'])
def delta():
    print('Tratador de requisição.')
    if request.method == 'POST':
        print('Pegando...')
        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
    else:
        print('Mandando...')
        a = int(request.args.get['a'])
        b = int(request.args.get['b'])
        c = int(request.args.get['c'])
    return f"O delta de X é {b**2-4*a*c}"

if __name__ == '__main__':
    aplicacao.run(host='0.0.0.0', port=5000)