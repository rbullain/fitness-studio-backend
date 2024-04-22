from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.accounts.serializers import UserProfileSerializer


class UserProfileView(APIView):
    """"""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_user = request.user
        serializer = UserProfileSerializer(current_user)
        return Response(serializer.data)
