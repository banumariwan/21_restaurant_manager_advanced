from django.db import models


class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    status = models.CharField(max_length=20,choices=[('free','free'),('occupied','occupied')])


    def __str__(self):
        return f"Table {self.number} - ({self.seats} Seats)"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    available = models.CharField(max_length=100,choices=[('Yes','Yes'), ('No','No')])


    def __str__(self):
        return self.name



class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField(MenuItem)
    status = models.CharField(max_length=100,choices=[("Pending", "Pending"), ("served", "served")])


    def __str__(self):
        return f"Order {self.id} - Table {self.table.number} - {self.status}"