# Generated by Django 5.1.6 on 2025-03-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='accounts/images/%Y/%m/%d/'),
        ),
    ]
