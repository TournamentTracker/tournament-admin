# Generated by Django 3.1.7 on 2022-04-12 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TournamentTracker', '0006_auto_20220410_1343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='school',
            name='points',
        ),
        migrations.CreateModel(
            name='SchoolPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(default=0)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TournamentTracker.school')),
            ],
            options={
                'ordering': ('points',),
            },
        ),
        migrations.AlterField(
            model_name='tournament',
            name='schools',
            field=models.ManyToManyField(blank=True, related_name='tournaments', to='TournamentTracker.SchoolPoints'),
        ),
    ]
