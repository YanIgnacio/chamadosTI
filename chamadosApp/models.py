from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count



# Create your models here.
class Tipo(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome do Serviço', blank=True)
    sigla = models.CharField(max_length=3, verbose_name="Sigla", blank=True)
    descricao = models.TextField(default='')
    
    def __str__(self):
        return self.nome
    
class Secretaria(models.Model):
    nome = models.CharField(max_length=70)

    def total_chamados(self):
        chamados_por_tipo = Chamado.objects.filter(secretaria=self).values('tipo__nome').annotate(total=Count('tipo')).order_by('tipo')
        return chamados_por_tipo

    def __str__(self):
        return self.nome

class Setor(models.Model):
    secretaria = models.ForeignKey(Secretaria, verbose_name="Secretaria", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default='')
    cep = models.CharField(max_length=8, default='')
    bairro = models.CharField(max_length=50, default='')
    logradouro = models.CharField(max_length=150, default='')

    def total_chamados(self):
        chamados_por_tipo = Chamado.objects.filter(setor=self).values('tipo__nome').annotate(total=Count('tipo')).order_by('tipo')
        return chamados_por_tipo
    
    def __str__(self):
        return self.nome
    
class Servidor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=75)
    email = models.EmailField(max_length=254, default='')
    setor = models.ForeignKey(Setor, verbose_name='Setor', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Atendente(Servidor):
    tipo = models.ManyToManyField(Tipo, verbose_name='Tipo')    
    
class Chamado(models.Model):
    
    prioridadeChoices = (
        ('0', 'Baixa'),
        ('1', 'Média'),
        ('2', 'Alta')
    )
    
    statusChoices = (
        ('0', 'Aberto'),
        ('1', 'Pendente'),
        ('2', 'Finalizado'),
    )
    
    secretaria = models.ForeignKey(Secretaria, verbose_name='Secretaria', on_delete=models.CASCADE, null=True)
    setor = models.ForeignKey(Setor, verbose_name='Setor', on_delete=models.CASCADE, null=True)
    requisitante = models.ForeignKey(Servidor, on_delete=models.CASCADE, related_name='requisitante')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=150)
    prioridade = models.CharField(max_length=1, choices=prioridadeChoices, default='0')
    status = models.CharField(max_length=1, choices=statusChoices, default='0')
    descricao = models.TextField(default='')
    atendente = models.ForeignKey(Atendente, verbose_name='Atendente', on_delete=models.CASCADE, related_name='atendente', null=True, default=None)
    dataAbertura = models.DateTimeField(auto_now_add=True)
    dataFechamento = models.DateTimeField(null=True, blank=False)
    numero = models.CharField(max_length=10, default=0)
    anexo = models.ImageField(upload_to='images', default=None, null=True, blank=True)
    
    def getPrioridade(self):
        for choice in self.prioridadeChoices:
            if choice[0] == self.prioridade:
                return choice[1]
        return "Desconhecido"
    
    def getStatus(self):
        for choice in self.statusChoices:
            if choice[0] == self.status:
                return choice[1]
        return "Desconhecido"
    
    def setNumero(self):
        ultimoChamado = Chamado.objects.last()
        if ultimoChamado:
            self.numero = str((int(ultimoChamado.numero) + 1)).zfill(5)
        else:
            self.numero = '00001'
        self.save()


class Comentario(models.Model):
    chamado = models.ForeignKey(Chamado, verbose_name='Chamado', on_delete=models.CASCADE)
    quemComentou = models.ForeignKey(Servidor, verbose_name='quemComentou', on_delete=models.CASCADE)
    dataHora = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(default='')
    confidencial = models.BooleanField(default=False)