# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_hooks', '0002_swappable_hook_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Hook',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]