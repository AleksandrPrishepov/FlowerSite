# Generated by Django 4.1.1 on 2022-09-15 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0003_alter_category_options_alter_flower_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категории растений', 'verbose_name_plural': 'Категории растений'},
        ),
        migrations.AlterField(
            model_name='category',
            name='n_cat',
            field=models.CharField(db_index=True, max_length=150, verbose_name='категории'),
        ),
    ]
