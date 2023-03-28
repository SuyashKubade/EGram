# Generated by Django 4.0.6 on 2023-03-27 17:47

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
            name='Child',
            fields=[
                ('childid', models.IntegerField(primary_key=True, serialize=False)),
                ('childname', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.DateField(max_length=10)),
                ('fathername', models.CharField(max_length=10)),
                ('mothername', models.CharField(max_length=10)),
                ('birthplace', models.CharField(max_length=10)),
                ('registeredon', models.CharField(max_length=10)),
                ('birthproof', models.FileField(null=True, upload_to='birthproof/')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('district_id', models.IntegerField(primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyHead',
            fields=[
                ('familyheadid', models.IntegerField(primary_key=True, serialize=False)),
                ('familyheadgender', models.CharField(max_length=6)),
                ('birthdate', models.DateField()),
                ('familyheadmobno', models.CharField(max_length=10)),
                ('familyheadadharno', models.CharField(max_length=12)),
                ('familyheadpanno', models.CharField(max_length=10)),
                ('familyheadphoto', models.FileField(null=True, upload_to='family_head/')),
                ('familyincome', models.CharField(max_length=15)),
                ('rationcardtype', models.CharField(max_length=10)),
                ('rationcardno', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Grampanchayat',
            fields=[
                ('gramid', models.IntegerField(primary_key=True, serialize=False)),
                ('gramname', models.CharField(max_length=50, unique=True)),
                ('gramaddress', models.TextField(max_length=100)),
                ('gramemail', models.EmailField(max_length=254)),
                ('gramcontact', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Housetax',
            fields=[
                ('housetypeid', models.IntegerField(primary_key=True, serialize=False)),
                ('housetype', models.CharField(max_length=30)),
                ('hosetaxrate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTax',
            fields=[
                ('watertaxid', models.IntegerField(primary_key=True, serialize=False)),
                ('waterconnectiontype', models.CharField(max_length=10)),
                ('watertaxrate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WaterConnection',
            fields=[
                ('waterconnectionid', models.IntegerField(primary_key=True, serialize=False)),
                ('waterconnectiontype', models.CharField(max_length=10)),
                ('ownername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.familyhead')),
            ],
        ),
        migrations.CreateModel(
            name='Taluka',
            fields=[
                ('taluka_id', models.IntegerField(primary_key=True, serialize=False)),
                ('taluka_name', models.CharField(max_length=50)),
                ('district_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.district')),
                ('state_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('houseid', models.IntegerField(primary_key=True, serialize=False)),
                ('houseno', models.IntegerField(unique=True)),
                ('region', models.CharField(max_length=20)),
                ('subregion', models.CharField(max_length=20)),
                ('housetype', models.CharField(max_length=20)),
                ('housearea', models.IntegerField()),
                ('gram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.grampanchayat')),
                ('ownername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.familyhead')),
            ],
        ),
        migrations.CreateModel(
            name='Gramadmin',
            fields=[
                ('gramadminid', models.IntegerField(primary_key=True, serialize=False)),
                ('gramadminmobno', models.CharField(max_length=10)),
                ('gramadminphoto', models.FileField(null=True, upload_to='gramadmin/')),
                ('grampanchayat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.grampanchayat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Familymembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familymemberid', models.IntegerField()),
                ('familymembername', models.CharField(max_length=40)),
                ('relation', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('birthdate', models.DateField()),
                ('aadharnop', models.CharField(max_length=12)),
                ('familymemberphoto', models.FileField(null=True, upload_to='family_member/')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.familyhead')),
                ('grampanchayat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.grampanchayat')),
            ],
        ),
        migrations.AddField(
            model_name='familyhead',
            name='grampanchayat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.grampanchayat'),
        ),
        migrations.AddField(
            model_name='familyhead',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='district',
            name='state_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.state'),
        ),
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('authorityid', models.IntegerField(primary_key=True, serialize=False)),
                ('authority', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('aadharnop', models.CharField(max_length=12)),
                ('qualification', models.CharField(max_length=20)),
                ('authoritynmobno', models.CharField(max_length=10)),
                ('authorityphoto', models.FileField(null=True, upload_to='authority/')),
                ('grampanchayat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramapp.grampanchayat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
