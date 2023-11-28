from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.auth.serializers import SignUpSerializer


class SignUpView(APIView):
    """API View to handle user sign up."""
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_content = {
                'id': user.pk,
                'message': 'User created successfully.',
            }
            return Response(response_content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
