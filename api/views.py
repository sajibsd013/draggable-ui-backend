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
        newdata = {
            "cv": request.data['cv'],
            "user": request.user.id
        }

        serializer = CVSerializer(data=newdata)
        print(serializer.is_valid(), request.user.id, request.data['cv'])
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

@api_view(['POST', 'GET', 'PUT','DELETE'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JWTAuthentication,))
def cv_detail(request, pk):
    try:
        data = CV.objects.get(pk=pk)
    except data.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CVSerializer(data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        newdata = {
            "cv": request.data['cv'],
            "user": request.user.id
        }
        print(newdata)
        serializer = CVSerializer(
            data, data=newdata)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
