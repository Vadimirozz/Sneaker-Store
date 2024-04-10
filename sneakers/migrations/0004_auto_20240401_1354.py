# Generated by Django 3.2.25 on 2024-04-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0003_alter_sneakers_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10, verbose_name='Size')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.AddField(
            model_name='sneakers',
            name='sizes',
            field=models.ManyToManyField(to='sneakers.Size', verbose_name='Available Sizes'),
        ),
    ]
