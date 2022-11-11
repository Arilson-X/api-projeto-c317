from django.contrib import admin
from django.urls import path, include
from sistema.views import ProdutosViewSet, ProdutoresViewSet, PedidoViewSet, RelatorioViewSet, \
    ListaPedidosProdutorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtor', ProdutoresViewSet, basename='Produtores')
router.register('produto', ProdutosViewSet, basename='Produtos')
router.register('pedido', PedidoViewSet, basename='Pedidos')
router.register('relatorio', RelatorioViewSet, basename='Relatorio')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('produtor/<int:pk>/pedidos/', ListaPedidosProdutorViewSet.as_view())
]
