# Generated by Django 4.2 on 2023-04-19 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_rename_bookid_books_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_id',
            field=models.IntegerField(),
        ),
    ]
