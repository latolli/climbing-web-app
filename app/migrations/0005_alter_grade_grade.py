# Generated by Django 4.0 on 2022-01-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_grade_grade_alter_grade_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.IntegerField(),
        ),
    ]