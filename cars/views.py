from rest_framework.views import APIView, Response, Request, status
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404


class CarView(APIView):
    def get(self, _: Request) -> Response:
        cars = Car.objects.all()
        car_list = CarSerializer(cars, many=True)
        return Response(car_list.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = Car.objects.create(**serializer.validated_data)
        car.save()

        serializer = CarSerializer(instance=car)
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class CarDetailView(APIView):
    def get(self, _: Request, car_id: int) -> Response:
        car = get_object_or_404(Car, id=car_id)
        serializer = CarSerializer(car)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request: Request, car_id: int) -> Response:
        car = get_object_or_404(Car, id=car_id)
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        for key, value in serializer.validated_data.items():
            setattr(car, key, value)

        car.save()
        serializer = CarSerializer(car)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def delete(self, request: Request, car_id: int):
        car = get_object_or_404(Car, id=car_id)
        car.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)