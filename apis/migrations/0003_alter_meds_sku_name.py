# Generated by Django 3.2.9 on 2021-11-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_meds_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meds',
            name='sku_name',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
    ]
