from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """TEst API view"""
    
    serializers_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses http methods as functions (get, post, patch, put, delete',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manuallt to URLs',
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})
    
    def post(self, request, format=None):
        """Create a hello message with our name"""

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
    def put(self, requset, pk=None):
        """Handle updating an object"""
        return Response({'method': "PUT"})

    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializers_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'aaa',
            'bbb',
            'ccc'
        ]

        return Response({'messsage':'Hello', 'a_viewset':a_viewset})
    
    def create(self,request):
        """Create a new gello message"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message}) 
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        """Getting an object by its id"""
        
        return Response({'http_method':'GET'}) 

    def update(self, request, pk=None):
        """Update an object by its id"""
        
        return Response({'http_method':'PUT'}) 
    
    def partial_update(self, request, pk=None):
        """Partial update of an object by its id"""
        
        return Response({'http_method':'PATCH'}) 

    def destroy(self, request, pk=None):
        """Delete an object by its id"""
        
        return Response({'http_method':'DELETE'}) 

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updating user profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)