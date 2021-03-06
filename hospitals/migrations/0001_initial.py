# Generated by Django 3.0.8 on 2020-07-06 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('total_beds', models.SmallIntegerField()),
                ('address', models.CharField(max_length=1500)),
                ('pincode', models.CharField(max_length=6)),
                ('phone_area_code', models.CharField(max_length=6)),
                ('contact', models.CharField(max_length=10)),
                ('country_code', models.CharField(default='+91', max_length=5)),
                ('admin', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=10)),
                ('country_code', models.CharField(default='+91', max_length=5)),
                ('adhaar_number', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('admission_timestamp', models.DateTimeField(auto_now=True)),
                ('discharge_timestamp', models.DateTimeField(editable=False, null=True)),
                ('discharged', models.BooleanField(default=False)),
                ('admitted_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.Hospital')),
            ],
        ),
    ]
