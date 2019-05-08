from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, id):
    try:
        q = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid:
            q = form.save()
            url = q.get_url
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question' : q.id})
    return render(request, 'question.html', {'question': q,
                                             'form' : form})
    

def index(request):   

    questions = Question.objects.new()
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
    	page = 1
    paginator = Paginator(questions, 10)
    page = paginator.page(page)
    return render(request, 'main.html', {
        'Title' : 'Latest',
        'paginator' : paginator,
        'questions' : page.object_list,
        'page' : page
        })

def popular(request):
    try:
        page = int(request.GET.get("page"))
    except ValueError:
        page = 1
    questions = Question.objects.popular()
    paginator = Paginator(questions, 10)
    page = paginator.page(page)

    return render(request, 'main.html',
                  {'title': 'Popular',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page, })

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            q = form.save()
            url = q.get_url 
            return HttpResponseRedirect(url)
    else:
        form = AskForm(initial={'question' : q.id})
    return render(request, 'ask.html', {'form' : form})

