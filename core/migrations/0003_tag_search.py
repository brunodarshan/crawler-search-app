# Generated by Django 2.2 on 2019-04-16 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='search',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Search'),
            preserve_default=False,
        ),
    ]
