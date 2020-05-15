from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name fields for testing APIview"""
    name = serializers.CharField(max_length=10, style={'base_template': 'textarea.html'})
    