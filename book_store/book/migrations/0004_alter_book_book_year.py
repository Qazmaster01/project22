# Generated by Django 5.1.2 on 2024-10-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_book_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_year',
            field=models.IntegerField(),
        ),
    ]
