from flask import Flask, request, jsonify
import calc

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    arg1 = request.args.get('x')
    arg2 = request.args.get('y')

    if arg1 is None or arg2 is None:
        return jsonify({'error': 'Missing parameters x and y'}), 400

    result = calc.add2(arg1, arg2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

