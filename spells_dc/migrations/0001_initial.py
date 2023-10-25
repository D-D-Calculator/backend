# Generated by Django 4.2.6 on 2023-10-25 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ability_scores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpellDc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_success', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200, null=True)),
                ('dc_type', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='spells', to='ability_scores.abilityscores')),
            ],
        ),
    ]
