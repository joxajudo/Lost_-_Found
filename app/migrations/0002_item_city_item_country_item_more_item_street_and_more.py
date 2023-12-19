# Generated by Django 4.2.7 on 2023-12-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='city',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='country',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='more',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='zipcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=1, max_digits=9),
            preserve_default=False,
        ),
    ]