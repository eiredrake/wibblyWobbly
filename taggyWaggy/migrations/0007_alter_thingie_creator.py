# Generated by Django 4.2.3 on 2023-07-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taggyWaggy', '0006_thingie_creator_thingie_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thingie',
            name='creator',
            field=models.CharField(max_length=255),
        ),
    ]