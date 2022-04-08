from django.contrib import admin
from myadmin.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display_links = ('id', 'username')
    #
    # # list_per_page设置每页显示多少条记录，默认是100条
    # list_per_page = 10

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)  # -id降序