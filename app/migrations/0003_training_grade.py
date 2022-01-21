# Generated by Django 4.0 on 2022-01-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0002_todolist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('trainingId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('gradeId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('grade', models.SmallIntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='auth.user')),
            ],
        ),
    ]