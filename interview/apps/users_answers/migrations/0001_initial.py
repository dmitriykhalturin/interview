# Generated by Django 2.2.13 on 2020-08-09 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='answers.Answer')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questions.Question')),
            ],
        ),
    ]
