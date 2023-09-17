# Generated by Django 4.2.5 on 2023-09-16 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('start_date', models.DateField(null=None)),
                ('end_date', models.DateField(null=None)),
                ('status', models.CharField(choices=[('Planned', 'planned'), ('In Progress', 'in progress'), ('On Hold', 'on hold'), ('Completed', 'completed')], max_length=30)),
                ('priority', models.CharField(choices=[('Low', 'low'), ('High', 'high'), ('Medium', 'medium')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.memberuser')),
                ('team_members', models.ManyToManyField(related_name='team_project', to='members.memberuser')),
            ],
        ),
    ]
