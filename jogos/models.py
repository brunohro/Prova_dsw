from django.db import models

class Modalidade(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    tipo = models.CharField()
    max_atletas = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    curso = models.CharField(max_length=50)
    cor = models.CharField()
    criada_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        return self.nome

class Tecnico(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=50)

    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE, related_name="equipe")

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()

    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, related_name="Equipe")

    modalidades = models.ManyToManyField(Modalidade, blank=True, related_name="Modalidade")

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.nome