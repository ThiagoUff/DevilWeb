from django.contrib import admin
from .models import Images, User, Produto, Categoria, Carrinho

admin.site.register(Images)
admin.site.register(User)
admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Carrinho)
