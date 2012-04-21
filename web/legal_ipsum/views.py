from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_GET

from markov import markov

files = markov.corpus_files()
chainer = markov.from_files(files)

@require_GET
def text(request):
    count = request.GET.get('count', 0)
    try:
        count = int(count)
    except ValueError:
        count = 0

    paragraphs = [chainer.paragraph(3, 3) for i in range(count)]
    ctx = {'paragraphs': paragraphs}
    return render(request, 'legal_ipsum/text.html', ctx)
