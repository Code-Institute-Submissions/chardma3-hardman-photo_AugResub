from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def permission_denied_view(request, exception):
    return render(request, '403.html', status=403)


def bad_request_view(request, exception):
    return render(request, '400.html', status=400)


def server_error_view(request, exception):
    return render(request, '500.html', status=500)
