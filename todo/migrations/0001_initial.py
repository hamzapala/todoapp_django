# Generated by Django 4.0.4 on 2022-05-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
                ('priority', models.CharField(choices=[('1', 'high'), ('2', 'medium'), ('3', 'low')], default='3', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Todos',
            },
        ),
    ]