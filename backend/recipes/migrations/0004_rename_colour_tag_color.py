# Generated by Django 3.2.13 on 2022-10-06 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_quantity_ingredientrecipe_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='colour',
            new_name='color',
        ),
    ]
