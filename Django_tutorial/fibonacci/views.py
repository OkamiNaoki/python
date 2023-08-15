from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View

class FibonacciView(View):
    def get(self, request, *args, **kwargs):
        try:
            n = int(request.GET.get('n', 0))
            if n < 0:
                return HttpResponseBadRequest("Invalid value for n")
            
            result = self.calculate_fibonacci(n)
            return JsonResponse({'result': result})
        except ValueError:
            return self.error_response(status=400, message="Bad request.")
    
    def calculate_fibonacci(self, n):
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
    
    def error_response(self, status, message):
        return JsonResponse({'status': status, 'message': message}, status=status)
