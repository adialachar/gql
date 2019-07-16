from .models import MyUser, Profile
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class MyUserNode(DjangoObjectType):
    class Meta:
        model = MyUser
        filter_fields = ('email',)
        interfaces = (Node, )
        #connection_class = Connection
class ProfileNode(DjangoObjectType):

    class Meta:
        model=Profile
        filter_fields = ('first_name','last_name',)
        interfaces = (Node, )
        #connection_class = Connection

class Query(ObjectType):

    user = Node.Field(MyUserNode)
    profile = Node.Field(ProfileNode)

    all_users = DjangoFilterConnectionField(MyUserNode)
    all_profiles = DjangoFilterConnectionField(ProfileNode)

schema = Schema(query=Query)
