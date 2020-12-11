# Generated by Django 3.1.3 on 2020-12-11 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20201207_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entries', related_query_name='entry', to='bboard.rubric', verbose_name='Рубрика'),
        ),
    ]
