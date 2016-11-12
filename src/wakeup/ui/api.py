from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from rest_framework import status



class SystemInfoViewSet(ViewSet):
    base_url = r'/session'
    base_name = ''

    def create(self, request):
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        if not request.user.is_authenticated():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if request.method == "GET":
            return Response({"username": request.user.username,"email":request.user.email})

    def retrieve(self, request, code=None):
        if not request.user.is_authenticated():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

