# Generated by Django 4.0.4 on 2022-04-23 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='only_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='chanel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.rating'),
        ),
    ]
