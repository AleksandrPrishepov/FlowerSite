# Generated by Django 4.1.1 on 2022-09-14 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_cat', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='flower',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='flower.category'),
        ),
    ]