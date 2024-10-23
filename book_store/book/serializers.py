from rest_framework import serializers

from .models import Author, Language, Genre, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(allow_null=True)
    # language = LanguageSerializer(allow_null=True)
    # genre = GenreSerializer(allow_null=True)

    class Meta:
        model = Book
        fields = "__all__"

class BookListAllSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(allow_null=True)
    language = LanguageSerializer(allow_null=True)
    genre = GenreSerializer(allow_null=True)

    class Meta:
        model = Book
        fields = "__all__"

        # model = Book
        # fields = '__all__'

    # def validate_title(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Заголовок должен содержать не менее 5 символов.")
    #     return value

    # def validate(self, attrs):
    #     title = attrs.get('title')
    #     amount_in_warehouse = attrs.get('amount_in_warehouse')
    #
    #     if amount_in_warehouse < 0:
    #         raise serializers.ValidationError("Количество на складе не может быть отрицательным.")
    #
    #     if title and title == "Запрещенное название":
    #         raise serializers.ValidationError("Заголовок не может быть 'Запрещенное название'.")
    #
    #     return attrs

