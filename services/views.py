from rest_framework import generics,viewsets,status
from rest_framework.response import Response

from services.permissions import ReadOnly
from .models import Category, Gallery, NoticePerson, Item, Order, OrderCourier, Person, PersonItem, Publicity, RatingPerson
from .serializers import CategorySerializer, GallerySerializer, NoticePersonSerializer, ItemSerializer, OrderCourierSerializer, OrderCourierStatusSerializer, OrderSerializer, OrderStatusSerializer, PersonItemSerializer, PersonSerializer, PublicitySerializer, RatingPersonSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnly]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnly]

class GalleryList(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [ReadOnly]

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [ReadOnly]

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class PublicityList(generics.ListCreateAPIView):
    queryset = Publicity.objects.all()
    serializer_class = PublicitySerializer

class PublicityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicity.objects.all()
    serializer_class = PublicitySerializer


class PersonItemViewSet(viewsets.ModelViewSet):
    queryset = PersonItem.objects.all()
    serializer_class = PersonItemSerializer
    
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class RatingPersonListCreateView(generics.ListCreateAPIView):
    queryset = RatingPerson.objects.all()
    serializer_class = RatingPersonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        person = serializer.validated_data['person']
        
        # Check if the user has already rated the item
        existing_rating = RatingPerson.objects.filter(user=user, person=person).first()
        if existing_rating:
            # If an existing rating is found, update it
            existing_rating.rating = serializer.validated_data['rating']
            existing_rating.save()
            return Response({"message": "Rating updated successfully"}, status=status.HTTP_200_OK)
        else:
            # If the user has not rated the item yet, create a new rating
            serializer.save(user=user)


class RatingPersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RatingPerson.objects.all()
    serializer_class = RatingPersonSerializer
    permission_classes = [IsAuthenticated]



class NoticePersonListCreateView(generics.ListCreateAPIView):
    queryset = NoticePerson.objects.all()
    serializer_class = NoticePersonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoticePersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoticePerson.objects.all()
    serializer_class = NoticePersonSerializer
    permission_classes = [IsAuthenticated]



class OrderCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [ReadOnly]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [ReadOnly]


class OrderStatusUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [ReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

class OrderCourierCreate(generics.ListCreateAPIView):
    queryset = OrderCourier.objects.all()
    serializer_class = OrderCourierSerializer
    permission_classes = [ReadOnly]


class OrderCourierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderCourier.objects.all()
    serializer_class = OrderCourierSerializer
    permission_classes = [ReadOnly]



class OrderCourierStatusUpdate(generics.UpdateAPIView):
    queryset = OrderCourier.objects.all()
    serializer_class = OrderCourierStatusSerializer
    permission_classes = [ReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)