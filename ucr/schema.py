from .models import MyUser, Profile
#from .repository import get_user, get_profile
import graphene
from graphene import ObjectType, relay, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

#class User(DjangoObjectType):
#    class Meta:
#        model = UserModel

class MyUserType(DjangoObjectType):
    class Meta:
      model = MyUser
  #    interfaces = (relay.Node,)

 #   @classmethod
  #  def get_user(cls, info, email):
   #     node = get_user(email)
    #    return node

class MyProfileType(DjangoObjectType):
    class Meta:
        model = Profile
   #     interfaces = (relay.Node,)

    #@classmethod
    #def get_profile(cls, info, email)
     #   node = get_profile(email)
      #  return node

class Query(ObjectType):
    users = graphene.List(MyUserType)

    profiles = graphene.List(MyProfileType)

    #node = relay.Node.field()

    def resolve_users(self,info):
        return MyUser.objects.all()

    def resolve_profiles(self,info):
        return Profile.objects.all()

schema = Schema(query=Query)


