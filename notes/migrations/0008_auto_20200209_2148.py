# Generated by Django 3.0.1 on 2020-02-09 14:48

from django.db import migrations
import notes.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20200131_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=notes.models.note_directory_path),
        ),
    ]
