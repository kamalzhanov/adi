from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Main
from .serializers import MainAPIViewSerializer
from rest_framework import viewsets, mixins
from .models import Main
from .serializers import MainViewSetSerializer

class MainAPIView(APIView):
    def get(self, request):
        items = Main.objects.all()
        serializer = MainAPIViewSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MainViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Main.objects.all()
    serializer_class = MainViewSetSerializer
