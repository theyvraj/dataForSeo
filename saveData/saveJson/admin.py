# search_app/admin.py
from django.contrib import admin
from .models import SearchResult

@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    list_display = ('search_id', 'keyword', 'search_time', 'status_code', 'result_count', 'cost')
    list_filter = ('status_code', 'search_time')
    search_fields = ('search_id', 'keyword')
    readonly_fields = ('search_id', 'full_response', 'search_time')
    
    # Add JsonField pretty formatting for the full_response field
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        return readonly_fields