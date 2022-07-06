from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

    #path('', views.index, name='index'),
    # Example of Dynamic URLs created with path converter: Added variable: question_id
    # Path converters are a simple method for capturing URL arguments
    # The dynamic title is now being generated from the URL.
    # the 'name' value is called by the {% url %} template tag in the index.html template file  
    # ex: /polls/5
    #path('<int:question_id>/', views.detail, name='detail'),
    #ex: /polls/5/results
    #path('<int:question_id>/results', views.results, name="results"),
