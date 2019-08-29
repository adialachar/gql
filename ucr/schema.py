from .models import MyUser, Profile
from .repository import get_user, get_profile
import graphene
from graphene import ObjectType, relay, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType


#class User(DjangoObjectType):
#    class Meta:
#        model = UserModel

class MyUserType(DjangoObjectType):
    class Meta:
      model = MyUser
      interfaces = (relay.Node, )

    #@classmethod
    #def get_user(cls, info, email):
     #   print(email)
     #   return MyUser.objects.get(email=email)
        #node = get_user(email)
        #return node


class MyProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        interfaces = (relay.Node,)

    #@classmethod
    #def get_profile(cls, info, email):
    #    node = get_profile(email)
    #    return node

class CreateUserAndProfile(graphene.Mutation):
    class Arguments:

        email = graphene.String()
        password = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()

    user = graphene.Field(MyUserType)
    profile = graphene.Field(MyProfileType)

    def mutate(self, info, email, password, first_name, last_name):
        u = MyUser.objects.create_user(email=email, password=password)
        p = Profile(user=u, first_name=first_name, last_name=last_name)
        p.save()

        return CreateUserAndProfile(user=u, profile=p)



class Mutation(ObjectType):
    create_user = CreateUserAndProfile.Field()




class Query(ObjectType):

    user = graphene.Field(MyUserType, email=graphene.String())

    users = graphene.List(MyUserType)

    profiles = graphene.List(MyProfileType)

    profile = graphene.Field(MyProfileType, email=graphene.String())

    node = relay.Node.Field()




    def resolve_users(self,info):
        return MyUser.objects.all()

    def resolve_user(self, info, email):
        print("HELLLOOOOOO")
        print(email)
        return MyUser.objects.get(email=email)

    def resolve_profile(self, info, email):
        u = MyUser.objects.get(email=email)
        return Profile.objects.get(user_id=u.id)

    def resolve_profiles(self,info):
        return Profile.objects.all()




schema = Schema(query=Query, mutation=Mutation)


