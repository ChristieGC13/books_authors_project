# Generated by Django 2.2.4 on 2021-03-23 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='book',
            new_name='books',
        ),
    ]
