# Generated by Django 3.2 on 2022-05-26 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('indoor', 'In Door'), ('outdoor', 'Out Door')], max_length=200, null=True)),
                ('description', models.TextField(blank=True, help_text='Detail Product', null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(help_text='Email: netuser979@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(help_text='Customer Name: Win Lin Tun', max_length=200),
        ),
    ]