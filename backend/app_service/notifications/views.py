from django.http import JsonResponse
from .models import Subscription

def subscribe(request):
    user = request.user
    department = request.GET['department']
    subscription, created = Subscription.objects.get_or_create(user=user, department=department)
    if created:
        return JsonResponse({'message': 'Subscribed successfully'})
    else:
        return JsonResponse({'message': 'Already subscribed'})

def unsubscribe(request):
    user = request.user
    department = request.GET['department']
    Subscription.objects.filter(user=user, department=department).delete()
    return JsonResponse({'message': 'Unsubscribed successfully'})
