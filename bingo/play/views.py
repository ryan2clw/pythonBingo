from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import random
from rest_framework import generics
from play.models import Card, Row
from play.serializers import CardSerializer, RowSerializer
from datetime import datetime

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class RowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

def seed_database():
    for i in range(6):
        #try:
        card = Card.objects.get_or_create(pk=i)
        print(card)
        for j in range(5):
            b = random.randint(1,16)
            i = random.randint(16,31)
            n = random.randint(31,46)
            g = random.randint(46,61)
            o = random.randint(61,76)
            row = Row.objects.create(b=b,i=i,n=n,g=g,o=o,card=card)
            row.save()

class RowList(generics.ListCreateAPIView):
    queryset = Row.objects.all()
    seed_database()
    serializer_class = RowSerializer


class RowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Row.objects.all()
    serializer_class = RowSerializer



