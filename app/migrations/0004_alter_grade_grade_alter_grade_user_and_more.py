# Generated by Django 4.0 on 2022-01-20 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0003_training_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='grade',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grade', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='training',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training', to='auth.user'),
        ),
    ]
