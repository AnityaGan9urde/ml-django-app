# Generated by Django 3.2.4 on 2021-06-25 07:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='updated')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('surname', models.CharField(max_length=255, verbose_name='surname')),
                ('email', models.EmailField(max_length=255, verbose_name='e-mail')),
                ('telephone', models.CharField(blank=True, max_length=20, verbose_name='telephone')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date of creation')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='natural persons register')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='updated')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='amount')),
                ('term', models.IntegerField(verbose_name='term')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='rate')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.client', verbose_name='client_id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='updated')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('payment', models.CharField(choices=[('made', 'made'), ('missed', 'missed')], default='missed', max_length=6, verbose_name='payment')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='amount')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.loan', verbose_name='loan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
