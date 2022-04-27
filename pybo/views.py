from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    quesiton_list = Question.objects.order_by('-create_date')
    context = {'question_list': quesiton_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    answer =Answer(Question=question, content=request.POST.get('content'),create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question_id)