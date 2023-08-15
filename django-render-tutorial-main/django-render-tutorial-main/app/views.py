from django.shortcuts import render

def fibonacci(request):
    n = 10  # Number of Fibonacci numbers to generate
    fibonacci_sequence = calculate_fibonacci(n)
    return render(request, 'fibonacci/fibonacci.html', {'fibonacci_sequence': fibonacci_sequence})

def calculate_fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)
    return sequence
