# Generated by Django 5.0.6 on 2024-06-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_chatmessage_file_chatmessagereaction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='call_time',
            field=models.CharField(blank=True, default='0', max_length=255, null=True),
        ),
    ]
