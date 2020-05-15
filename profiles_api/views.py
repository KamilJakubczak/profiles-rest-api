from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """TEst API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses http methods as functions (get, post, patch, put, delete',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manuallt to URLs',
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})