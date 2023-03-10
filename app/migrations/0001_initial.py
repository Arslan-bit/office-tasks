# Generated by Django 4.1.6 on 2023-02-09 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('pent', 'P'), ('shirt', 'S'), ('track soot', 'T')], max_length=10)),
                ('name', models.CharField(max_length=60)),
                ('tag', models.CharField(choices=[('recomened', 'R'), ('offer', 'O'), ('sale', 'S')], max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-update', '-create'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Add cart', 'AC'), ('cart cancel', 'CC'), ('pay cart', 'PC')], default='Add cart', max_length=20)),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-update', '-create'],
            },
        ),
    ]
