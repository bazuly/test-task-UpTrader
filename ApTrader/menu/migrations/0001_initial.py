# Generated by Django 5.0.4 on 2024-04-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.CharField(blank=True, max_length=128, null=True)),
                ('named_url', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]