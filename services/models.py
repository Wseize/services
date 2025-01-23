from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

    def __str__(self):
        return self.name
    
 
class RatingPerson(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField()

    class Meta:
        unique_together = ('user', 'person')

    def __str__(self):
        return f'{self.user.username} - {self.person.name} - {self.rating}'
    

    
class NoticePerson(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='notices')
    notice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f'{self.user.username} - {self.person.name} - {self.notice}'



class Person(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='persons', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.rating for rating in ratings) / ratings.count(), 2)
        return None

class Gallery(models.Model):
    person = models.ForeignKey(Person, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"Gallery image for {self.person.name}"
    



class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class PersonItem(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('person', 'item')

    def __str__(self):
        return f"{self.person.name} - {self.item.name} - {self.price}"


class Order(models.Model):
    RECEIVED = 'Received'
    IN_PROGRESS = 'In Progress'
    IN_TRANSIT = 'In Transit'
    COMPLETE = 'Complete'

    STATUS_CHOICES = [
        (RECEIVED, 'Received'),
        (IN_PROGRESS, 'In Progress'),
        (IN_TRANSIT, 'In Transit'),
        (COMPLETE, 'Complete'),
    ]


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=RECEIVED)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Order for {self.service.name} by {self.name}"

class Publicity(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='publicity/', null=True, blank=True)

    def __str__(self):
        return self.title
    



class OrderCourier(models.Model):
    RECEIVED = 'Received'
    IN_PROGRESS = 'In Progress'
    IN_TRANSIT = 'In Transit'
    COMPLETE = 'Complete'

    STATUS_CHOICES = [
        (RECEIVED, 'Received'),
        (IN_PROGRESS, 'In Progress'),
        (IN_TRANSIT, 'In Transit'),
        (COMPLETE, 'Complete'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=RECEIVED)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objectSent = models.CharField(max_length=255) 
    pickup_address = models.CharField(max_length=255) 
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    
    delivery_address = models.CharField(max_length=255) 
    delivery_latitude = models.FloatField()
    delivery_longitude = models.FloatField()

    delivery_time = models.DateTimeField(blank=True, null=True) 
    recipient_phone = models.CharField(max_length=20)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=3.25)

    def __str__(self):
        return f"Order for {self.user} | Status: {self.status}"
