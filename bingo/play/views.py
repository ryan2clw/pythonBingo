from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from play.models import Card, Row
from play.serializers import CardSerializer, RowSerializer

@api_view(['GET', 'POST'])
def card_list(request):
    """
    List all cards, or create a new card.
    """
    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def row_list(request):
    """
    List all rows, or create a new card.
    """
    if request.method == 'GET':
        rows = Row.objects.all()
        serializer = RowSerializer()
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RowSerializer(data=request.data)
        print(repr(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def ball_numbers(min, max):
    return range(min, max)