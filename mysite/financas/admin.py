from django.contrib import admin
from .models import Grupo
from .models import SubGrupo
from .models import Conta
from .models import Movimento

admin.site.register(Grupo)
admin.site.register(SubGrupo)
admin.site.register(Conta)
admin.site.register(Movimento)