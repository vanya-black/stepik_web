from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def question(request, id):
    '''
    try:
        q = Question.objects.get(id=id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question.html', {'question': q})
    '''
    return HttpResponse("Here's the text of the Web page.")

def index(request):
    '''
    questions = Question.objects.new()
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    paginator = Paginator(question, 10)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'main.html', {
        'Title' : 'Latest',
        'paginator' : paginator,
        'questions' : page.object_list,
        'page' : page
        })
        '''
    return HttpResponse("Here's the text of the Web page.")

def popular(request):
    '''
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
                '''
    return HttpResponse("Here's the text of the Web page.")

