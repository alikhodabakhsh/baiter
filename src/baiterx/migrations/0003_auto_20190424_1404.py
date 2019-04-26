# Generated by Django 2.1.7 on 2019-04-24 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baiterx', '0002_auto_20190424_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('B', 'Buy'), ('S', 'Sell')], default='B', help_text='buy or sell', max_length=1),
        ),
    ]