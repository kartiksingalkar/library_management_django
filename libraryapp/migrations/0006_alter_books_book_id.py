# Generated by Django 4.2 on 2023-04-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_alter_books_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_id',
            field=models.IntegerField(),
        ),
    ]
