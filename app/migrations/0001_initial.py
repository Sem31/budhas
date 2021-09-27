# Generated by Django 3.2.7 on 2021-09-26 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('giftTitle', models.CharField(blank=True, max_length=255, null=True)),
                ('giftDetail', models.TextField()),
                ('giftImage', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='LandingPageDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productHeading', models.CharField(blank=True, max_length=255, null=True)),
                ('productDetail', models.TextField()),
                ('productImage', models.ImageField(upload_to='uploads/')),
                ('actuallPrice', models.IntegerField()),
                ('percentage', models.IntegerField()),
                ('offerTime', models.IntegerField()),
                ('image_1', models.ImageField(upload_to='uploads/')),
                ('image_2', models.ImageField(upload_to='uploads/')),
                ('image_3', models.ImageField(upload_to='uploads/')),
                ('idolImage', models.ImageField(upload_to='uploads/')),
                ('idolName', models.CharField(blank=True, max_length=255, null=True)),
                ('idolDetail', models.TextField()),
                ('idolMaterial', models.CharField(blank=True, max_length=255, null=True)),
                ('idolColor', models.CharField(blank=True, max_length=255, null=True)),
                ('idolWeight', models.CharField(blank=True, max_length=255, null=True)),
                ('idolSize', models.CharField(blank=True, max_length=255, null=True)),
                ('idolInches', models.CharField(blank=True, max_length=255, null=True)),
                ('idolQuote', models.TextField()),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.gift')),
            ],
        ),
    ]