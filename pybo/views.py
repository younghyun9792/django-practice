from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def index(request):
    quesiton_list = Question.objects.order_by('-create_date')
    context = {'question_list': quesiton_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)