from django.contrib import admin
from .models import CatCategory, CatArticle, DogCategory, DogArticle
# Register your models here.

class CatCategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
class CatArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat_breed')
class DogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'dog_breed')
class DogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name')


admin.site.register(CatArticle, CatArticleAdmin)
admin.site.register(CatCategory)
admin.site.register(DogCategory)
admin.site.register(DogArticle, DogArticleAdmin)




