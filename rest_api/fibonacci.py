from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

@app.route('/fibonacci/<int:n>', methods=['GET'])
def get_fibonacci_sequence(n):
    fib_sequence = fibonacci(n)
    return jsonify(fib_sequence)

if __name__ == '__main__':
    app.run(debug=True)
