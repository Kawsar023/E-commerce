# Generated by Django 4.2.4 on 2023-10-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0011_rename_product_image_category_category_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='produ_image',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]