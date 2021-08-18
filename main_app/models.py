from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
MEALS = (("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner"))

# Create your models here.


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("toys_detail", kwargs={"pk": self.id})


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"cat_id": self.id})


class Feeding(models.Model):
    # first positional argument overrides the label
    date = models.DateField("feeding date")
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set default value for meal to be 'B'
        default=MEALS[0][0],
    )
    # Creates a cat_id FK property
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # get_thing_display method returns the second item in the meal tuple
        return f"{self.get_meal_display()} on {self.date} for {self.cat}"

    # change the default sort
    class Meta:
        ordering = ["-date"]
