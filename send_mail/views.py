from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_function
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['POST'])
def send_alert(request):
    send_mail_function.delay()
    return Response({"Sending alert started"},status=200)
