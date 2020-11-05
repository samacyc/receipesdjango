from django.shortcuts import render
from .serializer import CategorySerializer , ReceipeSerializer , TestSerializer , INGREDIENTSerializer
from rest_framework import generics , viewsets
from .models import Category , Receipe , TEST , Ing , Ingredients , Ing

# Create your views here.


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer

class TestList(generics.ListAPIView):
    queryset = TEST.objects.all()

    serializer_class = TestSerializer

class IngredientList(generics.ListAPIView):
    queryset = Ingredients.objects.all()

    serializer_class = INGREDIENTSerializer

class ReceipeFilter(generics.ListAPIView):
    serializer_class = ReceipeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user = self.kwargs["id"]
       
        return Receipe.objects.filter(Ingredients__ing__id=user)

class ReceipeList(generics.ListAPIView):
    queryset = Receipe.objects.all()

    serializer_class = ReceipeSerializer


class PurchaseList(generics.ListAPIView):
    serializer_class = ReceipeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.kwargs["id"]
        print(user)
        return Receipe.objects.filter(categories=user)