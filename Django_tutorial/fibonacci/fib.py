from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

@app.route('/fib', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n'))
        if n < 1:
            return jsonify({'error': 'Invalid input. n must be a positive integer.'}), 400

        result = fibonacci(n)
        return jsonify({'result': result}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input. n must be a valid integer.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
