# Generated by Django 2.0.4 on 2018-04-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180425_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='for_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cell',
            name='price',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='cell',
            name='value',
            field=models.IntegerField(default=25000),
        ),
        migrations.AddField(
            model_name='game',
            name='board_width',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='cell',
            name='height',
            field=models.FloatField(default=0.5),
        ),
    ]
