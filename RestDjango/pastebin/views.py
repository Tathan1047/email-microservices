# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from pastebin.models import Snippet
from pastebin.serializers import SnippetModelSerializer


@csrf_exempt
def get_snippets(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            snippet = get_object_or_404(Snippet, pk=pk)
            serializer = SnippetModelSerializer(snippet)
        else:
            snippets = Snippet.objects.all()
            serializer = SnippetModelSerializer(snippets, many=True)

        return HttpResponse(JSONRenderer().render(serializer.data), status=200, content_type='application/json')


@csrf_exempt
#Esta funcion retorna en formato Json todos los registros de la tabla
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)
        return HttpResponse(JSONRenderer().render(serializer.data), status=200, content_type='application/json')#LE da formato al JSON

