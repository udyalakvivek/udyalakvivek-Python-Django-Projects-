# Generated by Django 5.1.1 on 2024-10-04 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myform", "0002_studentmodel_address_studentmodel_dob_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentmodel",
            name="email",
            field=models.EmailField(default="vivek@gmail.com", max_length=254),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="father_name",
            field=models.CharField(default="Pandey ji", max_length=30),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="first_name",
            field=models.CharField(default="Vivek", max_length=30),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="last_name",
            field=models.CharField(default="Pandey", max_length=30),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="middle_name",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="mobile_number",
            field=models.BigIntegerField(default="9565851570"),
        ),
        migrations.AlterField(
            model_name="studentmodel",
            name="roll_number",
            field=models.IntegerField(default="121"),
        ),
    ]
