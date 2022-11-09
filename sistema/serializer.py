from rest_framework import serializers
from sistema.models import Produtor, Produto, Pedido, Relatorio


class ProdutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtor
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class PedidoSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class RelatorioSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'