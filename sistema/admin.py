from django.contrib import admin
from sistema.models import Produto, Produtor, Pedido, Relatorio


class Produtores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'cpf', 'telefone')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Produtor, Produtores)


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'variedade', 'qualidade')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


admin.site.register(Produto, Produtos)


class Pedidos(admin.ModelAdmin):
    list_display = ('id', 'produtor', 'produto', 'quantidade', 'valor', 'data')
    list_display_links = ('id',)


admin.site.register(Pedido, Pedidos)


class Relatorios(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'data')
    list_display_links = ('id',)


admin.site.register(Relatorio, Relatorios)
