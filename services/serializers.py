from rest_framework import serializers

from accounts.serializers import CustomUserSerializer
from .models import Category, Gallery, Item, NoticePerson, Order, OrderCourier, Person, PersonItem, Publicity, RatingPerson





class RatingPersonSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = RatingPerson
        fields = ['id', 'user', 'person', 'rating']


class NoticePersonSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = NoticePerson
        fields = ['id', 'user', 'person', 'notice', 'created_at']

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    ratings = RatingPersonSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    notices = NoticePersonSerializer(many=True, read_only=True)
    gallery = GallerySerializer(many=True, read_only=True, source='gallery_images')

    class Meta:
        model = Person
        fields = ['id', 'name', 'category', 'image', 'phone_number', 'available', 'location', 'latitude', 'longitude', 'ratings', 'average_rating', 'notices', 'gallery', 'valide', 'expertise']

    def get_average_rating(self, obj):
        # Calculate store's own average rating
        person_average = obj.average_rating if obj.average_rating is not None else 0

        return person_average


class PersonItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonItem
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    person_items = PersonItemSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'description', 'image', 'available', 'person_items' ]


    def get_person_items(self, obj):
        person_items = PersonItem.objects.filter(item=obj)
        return PersonItemSerializer(person_items, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['person_items'] = self.get_person_items(instance)
        return representation


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'items']


class OrderSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    user_mobile = serializers.CharField(source='user.username', read_only=True)
    governorat = serializers.CharField(source='person.location', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'item', 'person', 'location', 'status', 'created_at', 'item_name', 'user_mobile', 'date_time', 'price', 'governorat']



class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

class PublicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicity
        fields = '__all__'

class OrderCourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCourier
        fields = ['id', 'user', 'status', 'created_at', 'objectSent', 'pickup_address', 'pickup_latitude', 'pickup_longitude', 'delivery_address', 'delivery_latitude', 'delivery_longitude', 'delivery_time', 'recipient_phone', 'price']
        read_only_fields = ['id', 'created_at']


class OrderCourierStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCourier
        fields = ['status']
