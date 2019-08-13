from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import random
from rest_framework import generics
from play.models import Card, Row
from play.serializers import CardSerializer, RowSerializer

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class RowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# @api_view(['GET', 'POST'])
# def card_list(request):
#     """
#     List all cards, or create a new card.
#     """
#     if request.method == 'GET':
#         cards = Card.objects.all()
#         if(cards.count() < 5):
#             print(cards)
#         serializer = CardSerializer(cards, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = CardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RowList(generics.ListCreateAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer


class RowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer

# @api_view(['GET', 'POST'])
# def row_list(request):
#     """
#     List all rows, or create a new card.
#     """
#     if request.method == 'GET':
#         rows = Row.objects.all()
#         print(rows)
#         serializer = RowSerializer(data=dict(rows))
#         if not serializer.is_valid():
#             print(serializer.errors)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = RowSerializer(data=request.data)
#         print(repr(serializer))
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# def seed_database():
#     global rows
#     rows = []
#     b = random.randint(1,16)
#     i = random.randint(16,31)
#     n = random.randint(31,46)
#     g = random.randint(46,61)
#     o = random.randint(61,76)
#     row = [b,i,n,g,o]
#     return b
    # for i in range(5):
    #     row = Row(b=b.pop(),i=i.pop(),n=n.pop(),g=g.pop(),o=o.pop(),card=i)
    #     rows.append(row)

    # bRange = range(1, 16);
    # return [str(n) for n in bRange]


