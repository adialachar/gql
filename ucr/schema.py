from .models import UserModel
import graphene
from graphene import ObjectType, Node, Schema
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(ObjectType):
    users = graphene.List(User)

    def resolve_users(self,info):
        return UserModel.objects.all()

schema = Schema(query=Query)





'''
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

class MyUserMutation(graphene.Mutation):
    class Arguments:

        email = graphene.String(required=True)

    my_user = graphene.Field(MyUserNode)

        def mutate(self, info, email):
            my_user =  MyUser.objects.get(pk=id)
            my_user.email = email
            my_user.save()

            return MyUserMutation(my_user = my_user)

class Mutation(ObjectType):
    create_my_user =  MyUserMutation.Field()





class Query(ObjectType):

    user = Node.Field(MyUserNode)
    profile = Node.Field(ProfileNode)

    all_users = DjangoFilterConnectionField(MyUserNode)
    all_profiles = DjangoFilterConnectionField(ProfileNode)

schema = Schema(query=Query)
'''
