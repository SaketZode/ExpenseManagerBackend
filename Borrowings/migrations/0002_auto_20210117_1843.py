# Generated by Django 3.0.3 on 2021-01-17 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Borrowings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowing',
            old_name='status',
            new_name='Status',
        ),
    ]