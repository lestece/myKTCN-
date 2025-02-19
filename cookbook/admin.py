from django.contrib import admin
from .models import Recipe, Comment, Rating
from django_summernote.admin import SummernoteModelAdmin


# Register the Recipe model in the Admin panel
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',), 'excerpt': ('description',)}
    list_filter = ('status', 'created_on', 'is_public')
    list_display = ('title', 'slug', 'status', 'created_on', 'is_public')
    search_fields = ('title', 'content')
    actions = ['make_public']
    summernote_fields = ('ingredients', 'method',)

    def make_public(self, request, queryset):
        queryset.update(is_public=True)


# Register the Comment model in the Admin panel
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    summernote_fields = ('body',)

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Register the Rating model in the Admin panel
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('user', 'recipe', 'rating')
    search_fields = ('recipe', 'user')



