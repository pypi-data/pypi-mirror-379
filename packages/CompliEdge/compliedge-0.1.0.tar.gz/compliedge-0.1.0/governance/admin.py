from django.contrib import admin
from .models import Policy, PolicyDocument, PolicyComment

class PolicyDocumentInline(admin.TabularInline):
    model = PolicyDocument
    extra = 1

class PolicyCommentInline(admin.TabularInline):
    model = PolicyComment
    extra = 1

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'status', 'created_by', 'created_at', 'published_at')
    list_filter = ('status', 'created_at', 'published_at')
    search_fields = ('title', 'description')
    inlines = [PolicyDocumentInline, PolicyCommentInline]
    readonly_fields = ('created_at', 'updated_at', 'approved_at', 'published_at')

@admin.register(PolicyDocument)
class PolicyDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'policy', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('name', 'policy__title')

@admin.register(PolicyComment)
class PolicyCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'policy', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username', 'policy__title')