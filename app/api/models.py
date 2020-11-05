from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.



class Category(models.Model) :
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to ="categories" )

    def __str__(self) : 
        return self.name


class Ing(models.Model) :
    ing_name = models.CharField(max_length=38)
    image = models.ImageField(upload_to ="ing" )
    def __str__(self) : 
        return self.ing_name


class Ingredients(models.Model) : 
    ing = models.ForeignKey(Ing , on_delete = models.CASCADE)
    quantity = models.IntegerField(blank=True , null=True)
    oheda = models.TextField(blank=True , null=True)

    def __str__(self) : 
        return self.ing.ing_name + str(self.quantity)


class Receipe(models.Model) : 
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to ="receipes" )
    categories = models.ForeignKey(Category , on_delete = models.CASCADE)
    text = models.TextField(blank=True)
    duration = models.IntegerField(blank=True , null= True)
    Ingredients = models.ManyToManyField(Ingredients)
    slider = ArrayField(models.CharField(max_length=200), blank=True , null=True)



    def __str__(self) : 
        return self.title


class TEST(models.Model) : 
    name = models.CharField(max_length=200)
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    def __str__(self):
        return self.name 

class Post(models.Model):
    name = models.CharField(max_length=200)
    tags = ArrayField(models.CharField(max_length=200), blank=True)