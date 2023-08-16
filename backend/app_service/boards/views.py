from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Board

def board_list(request):
    boards = Board.objects.all()
    board_data = [{'id': b.id, 'name': b.name} for b in boards]
    return JsonResponse({'boards': board_data})

def board_create(request):
    name = request.POST['name']
    board = Board.objects.create(name=name)
    return JsonResponse({'message': 'Board created successfully', 'id': board.id})

@csrf_exempt
def board_edit(request, board_id):
    if request.method == 'POST':
        name = request.POST['name']
        board = Board.objects.get(pk=board_id)
        board.name = name
        board.save()
        return JsonResponse({'message': 'Board edited successfully'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def board_delete(request, board_id):
    if request.method == 'POST':
        Board.objects.filter(pk=board_id).delete()
        return JsonResponse({'message': 'Board deleted successfully'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)