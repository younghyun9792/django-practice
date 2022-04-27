from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    quesiton_list = Question.objects.order_vy('-create_date')
    context = {'question_list': quesiton_list}
    return render(request, 'pybo/question_list.html', context)