from store_APIS.models import Book
from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'