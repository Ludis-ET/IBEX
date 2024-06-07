# Generated by Django 5.0.6 on 2024-06-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_blog_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(related_name='blogs', to='core.category'),
        ),
    ]