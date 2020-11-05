from rest_framework import serializers

from .models import Category , Receipe , TEST , Ingredients , Ing
from django.contrib.postgres.fields import ArrayField


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',  'name', 'image']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TEST
        fields ="__all__"
class IngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ing
        fields ="__all__"
class INGREDIENTSerializer(serializers.ModelSerializer):
    ing = IngSerializer( read_only=True)
    class Meta:
        model = Ingredients
        fields ="__all__"

class ReceipeSerializer(serializers.ModelSerializer):
    Ingredients = INGREDIENTSerializer(read_only=True, many=True)
    categories = serializers.SerializerMethodField()
    class Meta:
        model = Receipe
        fields ="__all__"
    def get_Ingredients(self , instance) : 
        return "test"
    def get_categories(self ,instance) : 
        test = instance
        
        return  str(test.categories)
    

