from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image_url',
        'datetime',
    )

    ordering = ('name',) # to do a reverse ordering just stick a minus 
                         # infront of the word 'name'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_number',
        'blog',
        'user_profile',
        'description',
        'datetime',
        )
    
    ordering = ('blog',)
    


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)

