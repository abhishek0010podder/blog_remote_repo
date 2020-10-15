from django.contrib import admin
from testapp.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status'] # displays the fields
    prepopulated_fields={'slug':('title',)} #autopopulates field slug based on the input provided for title
    list_filter=('status','author','publish','created') # filters based on the fields
    search_fields=('title','body') #search in title and body
    raw_id_fields=('author',) # search bsed on id matching author. Particularly useful when we have a large number of authors.
    date_hierarchy='publish'  # adds a navbar to our blog project
    ordering=['status','publish']


class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=['active','created','updated']
    search_fields=['name','email','body']



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
