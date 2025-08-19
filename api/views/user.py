from dj_rest_auth.views import PasswordResetView
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from turbodrf.views import TurboDRFViewSet

from api.models.user import User
from api.serializers.user import UserSerializer

class UserViewSet(TurboDRFViewSet):
    model = User
    serializer_class = UserSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Response({"detail": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)
        self.queryset = User.objects.filter(email=self.request.user.email)
        return self.queryset

    @action(detail=False, methods=['get'])
    def logged(self,request):
        if self.queryset is not None:
            return Response(UserSerializer(self.queryset[0]).data)
        return Response({"detail": "User not authenticated."})

    @action(detail=False, methods=['post'], url_path='logged/update')
    def logged_update(self,request):
        if self.queryset is not None:
            serializer = UserSerializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "User not authenticated."})
