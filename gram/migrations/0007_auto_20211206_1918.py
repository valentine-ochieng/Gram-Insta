# Generated by Django 3.2.9 on 2021-12-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0006_auto_20211206_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='like', max_length=10),
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='images',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]