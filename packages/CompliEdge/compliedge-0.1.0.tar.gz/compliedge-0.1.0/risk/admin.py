from django.contrib import admin
from .models import RiskCategory, Risk, RiskMitigation, RiskReview

class RiskMitigationInline(admin.TabularInline):
    model = RiskMitigation
    extra = 1

class RiskReviewInline(admin.TabularInline):
    model = RiskReview
    extra = 1

@admin.register(RiskCategory)
class RiskCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner', 'likelihood', 'impact', 'risk_score', 'priority', 'status', 'created_at')
    list_filter = ('category', 'priority', 'status', 'created_at')
    search_fields = ('title', 'description')
    inlines = [RiskMitigationInline, RiskReviewInline]
    readonly_fields = ('risk_score', 'created_at', 'updated_at')

@admin.register(RiskMitigation)
class RiskMitigationAdmin(admin.ModelAdmin):
    list_display = ('action', 'risk', 'owner', 'due_date', 'completed')
    list_filter = ('completed', 'due_date')
    search_fields = ('action', 'description')

@admin.register(RiskReview)
class RiskReviewAdmin(admin.ModelAdmin):
    list_display = ('risk', 'reviewer', 'review_date')
    list_filter = ('review_date',)
    search_fields = ('comments',)