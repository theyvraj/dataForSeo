# search_app/views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SearchResult

@csrf_exempt
def save_search_result(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            
            # Create a new SearchResult instance
            result = SearchResult(
                search_id=data['id'],
                keyword=data['data']['keyword'],
                full_response=data,  # Store the entire JSON response
                status_code=data['status_code'],
                result_count=data['result_count'],
                execution_time=float(data['time'].split()[0]),
                cost=data['cost']
            )
            
            # Save to database
            result.save()
            
            return JsonResponse({'success': True, 'message': 'Search result saved successfully'})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)