# Generated by Django 4.0 on 2022-01-20 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0005_alter_grade_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goalId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('done', models.BooleanField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goal', to='auth.user')),
            ],
        ),
    ]
