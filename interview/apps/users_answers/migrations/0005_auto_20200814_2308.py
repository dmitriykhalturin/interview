# Generated by Django 2.2.13 on 2020-08-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_answers', '0004_auto_20200814_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='user_id',
            field=models.IntegerField(db_index=True),
        ),
    ]
