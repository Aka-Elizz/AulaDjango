from django.db import models
from datetime import datetime


# Create your models here.
#criando a categoria prlos models
class Category(models.Model):
    #marcando o modo como campo de caracter(Charfield), Em seguida o tamanhnho maximo e o que vai ser exibido
    name = models.CharField(max_length=150, verbose_name="Nome")
    desc = models.TextField(
        verbose_name="Descrição",
        #a descriçao pode ficar em branco
        blank=True,
        null=True,
    )
    
    #funçaõ para sobrescrever os atributos 
    def __str__(self):
        return self.name

    #modifica os nomes
    class Meta:
       verbose_name = "Categoria"
       verbose_name_plural = "Categorias"



class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name="Cor")
    color_id = models.CharField(max_length=100, verbose_name="Código Cor")

    def __str__(self):
        return self.name

    class Meta:
       verbose_name = "Cor"
       verbose_name_plural = "Cores"




class Size(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tamanho", unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
       verbose_name = "Tamanho"
       verbose_name_plural = "Tamanhos"



class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name="Marca/Fabricante")
    
    def __str__(self):
        return self.name

    class Meta:
       verbose_name = "Marca/Fabricante"
       verbose_name_plural = "Marcas/Fabricantes"



class Product(models.Model):

    OPCOES_MODA = [
        ("UNISSEX", "Unissex"),
        ("FEMININA", "Feminina"),
        ("MASCULINA", "Masculina")
    ]

    name = models.CharField(max_length=200, verbose_name="Nome do Produto")
    description = models.TextField(verbose_name="Descrição do produto")
    price = models.FloatField(verbose_name="Preço")
    fashion = models.CharField(max_length=50, choices=OPCOES_MODA,
    default= "", blank=False, null=False, verbose_name="Moda")
    status = models.BooleanField(verbose_name="Disponível", default=True)
    stock = models.PositiveIntegerField(verbose_name="Estoque disponível")
    category = models.ForeignKey(Category, verbose_name="Categoria", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name="Marca/Fabricante", on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name="Cor", on_delete=models.CASCADE)
    size = models.ForeignKey(Size, verbose_name="Tamanho", on_delete=models.CASCADE)

    image = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    
    registration_date = models.DateTimeField(default=datetime.now,
    blank=False, editable=False, verbose_name="Data Cadastro")

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


