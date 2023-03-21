# Generated by Django 3.1.3 on 2023-03-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokes',
            name='joker_type',
            field=models.CharField(choices=[('NONE', 'None'), ('GREEN', 'Green'), ('BLACK', 'Black')], default='NONE', max_length=5),
        ),
        migrations.AlterField(
            model_name='jokes',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]