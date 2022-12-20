from django.http import JsonResponse

# Create your views here.

def index(self):
    return JsonResponse({'code':'Hola Mundo'})