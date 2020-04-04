# Generated by Django 2.1.7 on 2019-04-12 11:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0003_note_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='img',
            field=models.ImageField(default='ZinedineZidane.jpg', upload_to='notes-img'),
        ),
    ]
