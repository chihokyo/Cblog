# Generated by Django 2.2.6 on 2019-10-26 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='下一篇', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='previous_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='上一篇', to='posts.Post'),
        ),
    ]
