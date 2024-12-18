# Generated by Django 5.1.4 on 2024-12-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.CharField(default=0, max_length=10)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
