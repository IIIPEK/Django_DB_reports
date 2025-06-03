
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Report, Alert
from .forms import ReportForm, AlertForm
from django.db.models import Q

@login_required
def report_list(request):
    query = request.GET.get('q', '')
    reports = Report.objects.filter(created_by=request.user)
    alerts = Alert.objects.filter(created_by=request.user)

    if query:
        reports = reports.filter(Q(title__icontains=query) | Q(description__icontains=query))
        alerts = alerts.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'main/report_list.html', {
        'reports': reports,
        'alerts': alerts,
        'query': query,
    })

@login_required
def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk, created_by=request.user)
    report.delete()
    return redirect('main:index')

@login_required
def alert_delete(request, pk):
    alert = get_object_or_404(Alert, pk=pk, created_by=request.user)
    alert.delete()
    return redirect('main:index')

@login_required
def report_form_view(request, pk=None):
    if pk:
        report = get_object_or_404(Report, pk=pk, created_by=request.user)
    else:
        report = Report(created_by=request.user)

    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect('main:index')
    else:
        form = ReportForm(instance=report)

    return render(request, 'main/report_form.html', {'form': form})

@login_required
def alert_form_view(request, pk=None):
    if pk:
        alert = get_object_or_404(Alert, pk=pk, created_by=request.user)
    else:
        alert = Alert(created_by=request.user)

    if request.method == 'POST':
        form = AlertForm(request.POST, instance=alert)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect('main:index')
    else:
        form = AlertForm(instance=alert)

    return render(request, 'main/alert_form.html', {'form': form})
