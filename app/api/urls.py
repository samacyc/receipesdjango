from django.urls import path , re_path

from .views import CategoryList , ReceipeFilter , ReceipeList ,TestList , IngredientList , PurchaseList
urlpatterns = [
    path('category/', CategoryList.as_view() , name = "category"),
    path('receipe/<id>', ReceipeFilter.as_view() , name = "receipe"),
    path('receipe/', ReceipeList.as_view() , name = "receipe") ,
    path('test/', TestList.as_view() , name = "receipe"),
    path('ing/', IngredientList.as_view() , name = "receipe"),
    path('category/<id>', PurchaseList.as_view()),






   
]