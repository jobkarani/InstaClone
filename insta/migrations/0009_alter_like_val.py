# Generated by Django 3.2.7 on 2021-12-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0008_auto_20211208_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='val',
            field=models.CharField(choices=[('Unlike', 'Unlike'), ('Like', 'Like')], default='like', max_length=50),
        ),
    ]