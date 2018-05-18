from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Ci, Ciauthor


admin.site.register(Ci)
admin.site.register(Ciauthor)
admin.site.site_header = '小川流云的管理控制台'
admin.site.site_title = '西窗夜话'