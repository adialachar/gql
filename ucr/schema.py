from .models import MyUser
import graphene
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

#class User(DjangoObjectType):
#    class Meta:
#        model = UserModel

class MyUserType(DjangoObjectType):
    class Meta:
        model = MyUser


class Query(ObjectType):
    users = graphene.List(MyUserType)

    def resolve_users(self,info):
        return MyUser.objects.all()

schema = Schema(query=Query)


