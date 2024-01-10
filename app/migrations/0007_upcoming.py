# Generated by Django 4.0.4 on 2022-08-03 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upcoming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Author_Name', models.CharField(max_length=200)),
                ('img', models.ImageField(default=1, upload_to='pics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'verbose_name_plural': 'books',
            },
        ),
    ]
