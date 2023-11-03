# Generated by Django 4.2.5 on 2023-11-01 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=15)),
                ('proposal_summary', models.TextField()),
                ('project_planning', models.TextField()),
                ('financing', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='saved_proposals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=15)),
                ('proposal_summary', models.TextField()),
                ('project_planning', models.TextField()),
                ('financing', models.TextField()),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ProposalSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('position', models.PositiveIntegerField(default=0)),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.proposal')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='proposal',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
    ]