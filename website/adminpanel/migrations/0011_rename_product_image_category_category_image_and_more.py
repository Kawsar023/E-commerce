# Generated by Django 4.2.4 on 2023-10-24 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0010_rename_category_image_category_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='product_image',
            new_name='category_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
    ]