# Generated by Django 2.0.4 on 2018-11-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('se', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.IntegerField()),
                ('username', models.CharField(max_length=500)),
                ('up_flag', models.BooleanField(default=False)),
                ('down_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
