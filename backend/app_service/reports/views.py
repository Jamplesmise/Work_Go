from django.http import JsonResponse
from .models import Report

def summary(request):
    reports = Report.objects.all()
    summary_data = {'total_reports': reports.count()}
    return JsonResponse(summary_data)

def detail(request):
    report_id = request.GET['id']
    report = Report.objects.get(pk=report_id)
    detail_data = {'title': report.title, 'content': report.content}
    return JsonResponse(detail_data)
