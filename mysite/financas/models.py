from django.db import models

class Grupo(models.Model):
	descricao = models.CharField(max_length=50, null=False, blank=False)
	def __str__(self):
		ret = self.descricao
		return ret	

class SubGrupo(models.Model):
	descricao = models.CharField(max_length=50, null=False, blank=False)
	grupo = models.ForeignKey("Grupo", on_delete=models.CASCADE, related_name='codigo_grupo', null=True)
	def __str__(self):
		ret = self.descricao
		return ret	

class Conta(models.Model):
	SITUACAO_CONTA_CHOICES = (
		("A", "Ativa"),
		("I", "Inativa")
	)
	descricao = models.CharField(max_length=50, null=False, blank=False)
	banco = models.CharField(max_length=50, null=False, blank=False)
	agencia = models.CharField(max_length=50, null=False, blank=False)
	numero = models.CharField(max_length=50, null=False, blank=False)
	situacao = models.CharField(max_length=1, choices=SITUACAO_CONTA_CHOICES, null=False, blank=False)
	padrao = models.BooleanField(default=False)
	def __str__(self):
		ret = self.descricao
		return ret	

class Movimento(models.Model):
	TIPO_CHOICES = (
		("C", "Crédito"),
		("D", "Débito")
	)
	SITUACAO_MOVIMENTO_CHOICES = (
		("A", "Ativa"),
		("I", "Inativa")
	)
	descricao = models.CharField(max_length=500, null=False, blank=False)
	datageracao = models.DateTimeField(blank=False)
	dataefetivacao = models.DateTimeField(null=True, blank=True)
	conta = models.ForeignKey("Conta", on_delete=models.CASCADE, related_name='codigoconta', null=True)
	subgrupo = models.ForeignKey("SubGrupo", on_delete=models.CASCADE, related_name='codigosubgrupo', null=True)
	valor = models.DecimalField(default=0, null=False, blank=False, max_digits=12, decimal_places=2)
	tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, null=False, blank=False)
	situacao = models.CharField(max_length=1, choices=SITUACAO_MOVIMENTO_CHOICES, null=False, blank=False)
	codigotransferencia = models.IntegerField(default=0, null=False, blank=False)
	def __str__(self):
		ret = self.descricao
		return ret	
