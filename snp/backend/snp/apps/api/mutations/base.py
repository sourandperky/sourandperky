import graphene


class Base(graphene.relay.ClientIDMutation):
    class Meta:
        abstract = True
