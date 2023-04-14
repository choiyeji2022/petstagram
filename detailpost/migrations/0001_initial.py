# Generated by Django 4.2 on 2023-04-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('content', models.CharField(max_length=225, verbose_name='내용')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='작성시간')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
            options={
                'db_table': 'detail',
            },
        ),
    ]
