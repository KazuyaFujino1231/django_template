from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({'status': 'ok'})


class EchoView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        payload = request.data or {}
        return Response({'echo': payload}, status=status.HTTP_200_OK)
