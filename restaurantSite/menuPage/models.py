from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.TextField()

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100)
    food_description = models.TextField(blank=True, null=True)
    food_price = models.DecimalField(max_digits=10, decimal_places=2)
    food_thumbnail = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    food_items = models.ManyToManyField(FoodItem)

    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.IntegerField()
    table_status = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, related_name='tables', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('table_number', 'restaurant')

    def __str__(self):
        return f"Table {self.table_number} - {self.restaurant.name}"


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    items = models.JSONField()

    def __str__(self):
        return f"Order {self.pk} for Table {self.table.table_number} at {self.restaurant.name}"


class MenuPageAdministration(models.Model):
    color = models.CharField(
        max_length=50,
        default="None",
        choices=[
            ("none", "None"),
            ("blue", "Blue"),
            ("green", "Green"),
            ("purple", "Purple"),
            ("orange", "Orange"),
        ],
    )
    bg_image = models.CharField(max_length=255, null=True, default="None")