from datetime import datetime

from django.db import models


class Produtor(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    variedade = models.CharField(max_length=200)
    qualidade = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    quantidade = models.IntegerField(default=0)
    valor = models.FloatField(default=0)
    data = models.DateTimeField(default=datetime.now())
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.data


class Relatorio(models.Model):
    data = models.DateTimeField(default=datetime.now())
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.data



