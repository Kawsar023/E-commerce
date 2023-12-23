# Generated by Django 4.2.4 on 2023-11-26 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminpanel', '0018_product_produ_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_date', models.DateField(auto_now=True)),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminpanel.cuostomer')),
                ('prd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminpanel.product')),
            ],
        ),
    ]
