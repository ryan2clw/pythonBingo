from rest_framework import serializers
from play.models import Row
from play.models import Card
"""
Form the JSON that we need
"""
class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ['b', 'i', 'n', 'g', 'o', 'card']

class CardSerializer(serializers.ModelSerializer):
    rows = serializers.StringRelatedField(many=True)

    class Meta:
        model = Card
        fields = ['id', 'rows', 'created_on']
        depth = 1

    def create(self, validated_data):
        rows_data = validated_data.pop('rows')
        card = Card.objects.create(**validated_data)
        card.save()
        for row_data in rows_data:
            Row.objects.create(card=card, **row_data)
        return card

    def get_queryset(self):
        return Card.objects.all()