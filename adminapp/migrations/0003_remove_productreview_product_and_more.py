# Generated by Django 5.1.4 on 2024-12-13 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_address_productreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='ProductReview',
        ),
    ]
