# Generated by Django 5.1.1 on 2024-10-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myform", "0004_alter_studentmodel_mobile_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentmodel",
            name="dob",
            field=models.DateField(),
        ),
    ]
