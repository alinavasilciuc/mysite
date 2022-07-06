'''#from django.shortcuts import render
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.urls import reverse
from django.views import generic
#from django.db.models import F
#from django.template import loader'''

''' The view decides what data gets delivered to the template, either by 
    - acting on input from the user or 
    - in response to other business logic and internal processes. 
Each Django view performs a specific function and has an associated template. 
----------------------------------------------------------------------------------'''

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context={'question' : question,
             'error_message' : "You didn't select a choice"}            
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", context)
    else:    
        #selected_choice.votes += 1  # This way lets a race condition to happen because python is updating the values in the database
        selected_choice.votes = F('votes') +1 # This way avoids a race condition because the database updates the fields value instead of python
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 




''' def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    #context is a dictionary mapping template variable names to Python objects
    context = { "latest_question_list": latest_question_list,}
    return HttpResponse(template.render(context, request)) 
#Not using this view because we are using generic views from now on
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { "latest_question_list": latest_question_list}
    return render(request, 'polls/index.html', context)



# We dont use this way of coding because that would couple the model layer to the view layer. 
# One of the foremost design goals of Django is to maintain loose coupling. 
# Some controlled coupling is introduced in the django.shortcuts module.
#Same for index
def detail(request, question_id):
    try: 
        question = Question.objects.get(pk=question_id)
        context = {'question': question}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', context) 
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context={'question' : question}
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return(render(request, 'polls/results.html', {'question': question}))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context={'question' : question,
             'error_message' : "You didn't select a choice"}            
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", context)
    else:    
        #selected_choice.votes += 1  # This way lets a race condition to happen because python is updating the values in the database
        selected_choice.votes = F('votes') +1 # This way avoids a race condition because the database updates the fields value instead of python
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
'''

'''
- return HttpResponse("You are looking at the results of question %s" % question_id)
- request.POST values are always strings.
- request.POST is a dictionary-like object
- Django also provides request.GET
- you should always return an HttpResponseRedirect after successfully 
dealing with POST data
- We are using the reverse() function in the HttpResponseRedirect 
constructor in this example. This function helps avoid having to 
hardcode a URL in the view function. It is given the name of the view 
that we want to pass control to and the variable portion of the URL 
pattern that points to that view. In this case, using the URLconf we 
set up in Tutorial 3, this reverse() call will return a string like 
'/polls/3/results/'
- 
'''