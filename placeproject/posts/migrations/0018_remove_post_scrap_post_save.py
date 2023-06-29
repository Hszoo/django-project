# Generated by Django 4.2.1 on 2023-06-28 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_post_scrap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='scrap',
        ),
        migrations.CreateModel(
            name='Post_save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrap', models.BooleanField(default=False, verbose_name='게시글스크랩')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
