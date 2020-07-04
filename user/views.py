from datetime import datetime
from rest_framework import viewsets
from .models import User
from .serializers import GetUserSerializer


class User(viewsets.ModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
