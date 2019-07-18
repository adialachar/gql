from .models import MyUser, Profile
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

class MyProfileType(DjangoObjectType):
    class Meta:
        model = Profile

class Query(ObjectType):
    users = graphene.List(MyUserType)

    profiles = graphene.List(MyProfileType)

    def resolve_users(self,info):
        return MyUser.objects.all()

    def resolve_profiles(self,infor):
        return Profile.objects.all()

schema = Schema(query=Query)


