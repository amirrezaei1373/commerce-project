# Generated by Django 4.0.2 on 2022-03-03 13:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('starting_bid', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('closed', models.BooleanField(default=False)),
                ('category', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='category_for_the_auction', to='auctions.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_make_the_auction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
