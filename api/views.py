from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CV
from .serializers import CVSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['POST', 'GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def cv(request):
    if request.method == 'POST':
        serializer = CVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        try:
            cv = CV.objects.filter(user=request.user.id).order_by("-id")
            cvserializer = CVSerializer(cv, many=True)
            return Response(cvserializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
