# Generated by Django 4.2.4 on 2023-11-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0017_rename_user_img_user_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='produ_image',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
