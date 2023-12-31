# Generated by Django 4.2.3 on 2023-07-15 17:55

from django.db import migrations


def populate_role(apps, schemaeditor):
    entries = {
        "developer": "A team member who can complete issues",
        "scrum master": "The team's coach",
        "product ower": "Has ownership of the product",
    }
    Role = apps.get_model('accounts', 'Role')
    for name, description in entries.items():
        role_obj = Role(name=name, description=description)
        role_obj.save()


def populate_team(apps, schemaeditor):
    entries = {
        "alpha": "The A team",
        "bravo": "The B team",
        "charlie": "The C team",
        "delta": "The D team",
    }
    Team = apps.get_model('accounts', 'Team')
    for name, description in entries.items():
        team_obj = Team(name=name, description=description)
        team_obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_role),
        migrations.RunPython(populate_team),
    ]
