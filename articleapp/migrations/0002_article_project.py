# Generated by Django 3.2.4 on 2021-08-19 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_alter_project_created_at'),
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='projectapp.project'),
        ),
    ]
