# Generated by Django 2.2 on 2019-04-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanage', '0003_auto_20190428_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]