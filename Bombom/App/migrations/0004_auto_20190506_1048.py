# Generated by Django 2.2.1 on 2019-05-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_crush_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crush',
            name='signo',
            field=models.CharField(choices=[('áries', 'áries'), ('touro', 'touro'), ('gêmeos', 'gêmeos'), ('câncer', 'câncer'), ('leão', 'leão'), ('virgem', 'virgem'), ('libra', 'libra'), ('escorpião', 'escorpião'), ('sagitário', 'sagitário'), ('capricórnio', 'capricórnio'), ('aquário', 'aquário'), ('peixes', 'peixes')], max_length=12),
        ),
    ]
