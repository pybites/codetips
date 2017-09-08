from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from api.models import Tip
from api.serializers import TipSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly


class TipList(generics.ListCreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
