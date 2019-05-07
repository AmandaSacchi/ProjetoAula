from django.db import models

# Create your models here.
class Crush(models.Model):          #Proximo Passo: import no admin & views
    signo_opcoes = [
    ('áries', 'áries'),
    ('touro', 'touro'),
    ('gêmeos', 'gêmeos'),
    ('câncer', 'câncer'),
    ('leão', 'leão'),
    ('virgem', 'virgem'),
    ('libra', 'libra'),
    ('escorpião', 'escorpião'),
    ('sagitário', 'sagitário'),
    ('capricórnio', 'capricórnio'),
    ('aquário', 'aquário'),
    ('peixes', 'peixes')
    ]
    nome = models.CharField(max_length = 100)
    genero = models.CharField(max_length = 50)
    data = models.DateField()
    signo = models.CharField(max_length = 12, choices = signo_opcoes)
    qualidade = models.CharField(max_length = 100)
    defeito = models.CharField(max_length = 100, default = 'não está comigo')
    reciproco = models.BooleanField(default = False)
    solteiro = models.BooleanField(default = False)
    foto = models.ImageField(upload_to ='', null = True) #ADICIONAR em SETTINGS.PY > media_url
    def __str__(self):
        return self.nome