# Generated by Django 4.0.4 on 2022-08-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TournamentTracker', '0011_auto_20220421_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='cutoff_month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='September', max_length=10),
        ),
    ]
