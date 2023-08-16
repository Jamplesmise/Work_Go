# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSerializer



@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse({'message': 'Registered successfully', 'user_id': user.id})
        else:
            return JsonResponse({'message': 'Registration failed', 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'Logged in successfully'})
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status=400)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})
