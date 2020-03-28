# Generated by Django 3.0.3 on 2020-03-28 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rate', '0012_auto_20200326_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_to_the_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reportings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate.Message_to_the_user')),
            ],
        ),
    ]
