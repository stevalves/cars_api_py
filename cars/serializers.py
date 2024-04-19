from rest_framework import serializers

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=85)
    spec = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    fuel = serializers.CharField(max_length=85)
    km = serializers.IntegerField()
    color = serializers.CharField(max_length=85)
    fipe = serializers.IntegerField()
    description = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField(read_only=True)
