# Generated by Django 4.0.3 on 2022-04-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('username', models.TextField(primary_key=True, serialize=False)),
                ('keyword', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='key_word',
        ),
    ]
