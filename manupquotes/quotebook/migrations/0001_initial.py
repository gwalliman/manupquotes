# Generated by Django 2.1.5 on 2019-01-18 06:33

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
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('quote', models.TextField()),
                ('background', models.ImageField(upload_to='backgrouns/')),
                ('owner', models.ForeignKey(help_text='The user that submitted this quote', on_delete=django.db.models.deletion.DO_NOTHING, related_name='quotes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Quotes',
            },
        ),
    ]
