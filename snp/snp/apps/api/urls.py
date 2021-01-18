from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# We are going to remote the csrf_exempt here once we implement token authentication
urlpatterns = [
    path("", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
