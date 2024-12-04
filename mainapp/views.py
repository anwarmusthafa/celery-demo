from django.http import HttpResponse
from .tasks import test_func
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User

# View to test asynchronous task
def test(request):
    test_func.delay()
    return HttpResponse("Task triggered successfully.")

# API view for user registration
@api_view(['POST'])
@permission_classes([AllowAny])  # Allows unauthenticated access
def register(request):
    username = request.data.get('username')  # Fetching data from the request
    password = request.data.get('password')
    email = request.data.get('email')
    
    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)
    
    try:
        user = User.objects.create_user(username=username, password=password)
        if user:
            user.email = email
            user.save()  # Fixed the issue: Call the save() method as a function
        return Response({"message": "New User created successfully."}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=400)


