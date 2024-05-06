# Generated by Django 5.0.3 on 2024-04-22 10:29

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
                ('name', models.CharField(default='', max_length=255)),
                ('product', models.CharField(default='', max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=1000)),
                ('date_of_fabrication', models.DateField()),
                ('date_of_expiration', models.DateField()),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
            ],
        ),
    ]
