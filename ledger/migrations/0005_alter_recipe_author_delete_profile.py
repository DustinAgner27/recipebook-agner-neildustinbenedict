# Generated by Django 5.0.2 on 2024-03-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_alter_profile_short_bio_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]