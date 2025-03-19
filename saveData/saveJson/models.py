# search_app/models.py
from django.db import models
from django.db.models import JSONField  # For Django 3.1+

class SearchResult(models.Model):
    # Basic metadata fields
    search_id = models.CharField(max_length=255, unique=True)
    keyword = models.CharField(max_length=255)
    search_time = models.DateTimeField(auto_now_add=True)
    
    # Store the entire JSON response
    full_response = JSONField()
    
    # Optional: Add convenience fields for frequently accessed data
    status_code = models.IntegerField()
    result_count = models.IntegerField()
    execution_time = models.FloatField()
    cost = models.FloatField()
    
    def __str__(self):
        return f"Search for '{self.keyword}' ({self.search_id})"
    
    class Meta:
        ordering = ['-search_time']