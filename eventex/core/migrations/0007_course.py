# Generated by Django 4.0 on 2021-12-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_talk_options_alter_talk_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titulo')),
                ('start', models.TimeField(blank=True, null=True, verbose_name='inicio')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('slots', models.IntegerField()),
                ('speakers', models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes')),
            ],
            options={
                'verbose_name': 'palestra',
                'verbose_name_plural': 'palestras',
                'abstract': False,
            },
        ),
    ]
