# Generated by Django 4.0.2 on 2022-05-17 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Lastname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='last_name',
        ),
    ]