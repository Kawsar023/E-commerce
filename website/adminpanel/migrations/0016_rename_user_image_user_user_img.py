# Generated by Django 4.2.4 on 2023-11-05 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0015_alter_user_user_t_delete_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_image',
            new_name='user_img',
        ),
    ]
