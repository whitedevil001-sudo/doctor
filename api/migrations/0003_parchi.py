# Generated by Django 4.2 on 2023-04-21 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_doctors_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='parchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('time', models.TimeField()),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.doctors')),
            ],
        ),
    ]
