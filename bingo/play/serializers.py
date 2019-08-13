from rest_framework import serializers
from play.models import Row, Card, BingoBoard
"""
Form the JSON that we need
"""
class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ['b', 'i', 'n', 'g', 'o', 'card']

    def create(self, validated_data):
        rows_data = validated_data.pop('rows')
        card = Card.objects.create(**validated_data)
        card.save()
        for row_data in rows_data:
            Row.objects.create(card=card, **row_data)
        return card

    def get_queryset(self):
        return Row.objects.all()

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['id', 'created_on']
        depth = 1


        """
        So the model defines the table structure which is good,
        so then the serializer needs to return the row
        """