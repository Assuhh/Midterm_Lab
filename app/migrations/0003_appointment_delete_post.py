# Generated by Django 5.1.2 on 2024-12-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=100)),
                ('contact_number', models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
