# Generated by Django 3.2.7 on 2022-10-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_menu_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='nutrition',
            field=models.TextField(null=True),
        ),
    ]
