# Generated by Django 3.0.5 on 2020-04-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200402_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='third',
            name='MainTitle',
            field=models.CharField(default='At Your Service', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Template',
            field=models.CharField(default='Template 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Title',
            field=models.CharField(default='Your title here', max_length=200),
        ),
        migrations.AlterField(
            model_name='downloadsession',
            name='ButtonText',
            field=models.CharField(default='Download Now', max_length=100),
        ),
        migrations.AlterField(
            model_name='downloadsession',
            name='Description',
            field=models.TextField(blank=True, default='Text Here', max_length=200),
        ),
        migrations.AlterField(
            model_name='downloadsession',
            name='Title',
            field=models.CharField(default='Heading', max_length=100),
        ),
        migrations.AlterField(
            model_name='first',
            name='ButtonText',
            field=models.CharField(default='Find out more', max_length=20),
        ),
        migrations.AlterField(
            model_name='first',
            name='Description',
            field=models.TextField(default='We can help you build better websites using the Bootstrap CSS framework! Just download your template and start going, no strings attached!', max_length=300),
        ),
        migrations.AlterField(
            model_name='first',
            name='Title',
            field=models.CharField(default='The best startup ever', max_length=200),
        ),
        migrations.AlterField(
            model_name='images',
            name='ImagesName',
            field=models.CharField(default='Template 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='category1',
            field=models.CharField(blank=True, default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='category2',
            field=models.CharField(blank=True, default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='category3',
            field=models.CharField(blank=True, default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='category4',
            field=models.CharField(blank=True, default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='category5',
            field=models.CharField(blank=True, default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='category6',
            field=models.CharField(blank=True, default='Category', max_length=50),
        ),
        migrations.AlterField(
            model_name='images',
            name='title1',
            field=models.TextField(blank=True, default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='title2',
            field=models.TextField(blank=True, default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='title3',
            field=models.TextField(blank=True, default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='title4',
            field=models.TextField(blank=True, default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='title5',
            field=models.TextField(blank=True, default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='title6',
            field=models.TextField(blank=True, default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='second',
            name='ButtonText',
            field=models.CharField(default='Get started!', max_length=50),
        ),
        migrations.AlterField(
            model_name='second',
            name='Title',
            field=models.CharField(default="We've got what you need!", max_length=100),
        ),
    ]
