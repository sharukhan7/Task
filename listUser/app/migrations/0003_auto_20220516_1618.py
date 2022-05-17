# Generated by Django 3.1 on 2022-05-16 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220516_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('user_email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='corporate',
            name='corporate_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
    ]