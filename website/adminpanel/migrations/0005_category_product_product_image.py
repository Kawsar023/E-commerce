# Generated by Django 4.2.4 on 2023-09-19 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0004_rename_mobilenum_customer_mobile_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_new_price', models.FloatField()),
                ('product_old_price', models.FloatField()),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='adminpanel.category')),
            ],
        ),
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image_all', models.ImageField(blank=True, null=True, upload_to='product/')),
                ('product_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='adminpanel.product')),
            ],
        ),
    ]
