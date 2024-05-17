# Generated by Django 3.2.9 on 2021-12-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutureGlam', '0012_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(default='', max_length=50)),
                ('ttype', models.CharField(default='', max_length=50)),
                ('question', models.CharField(default='', max_length=50)),
                ('answer', models.CharField(default='', max_length=50)),
                ('option1', models.CharField(default='', max_length=50)),
                ('option2', models.CharField(default='', max_length=50)),
                ('option3', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
