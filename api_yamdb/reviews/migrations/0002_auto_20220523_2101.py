# Generated by Django 2.2.16 on 2022-05-23 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('-id',)},
        ),
        migrations.RemoveConstraint(
            model_name='review',
            name='unique_review',
        ),
    ]
