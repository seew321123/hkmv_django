# Generated by Django 3.0.3 on 2020-02-25 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20200225_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment_in_comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment_in_comment',
            name='owner',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]