from graphene import relay, ObjectType

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from cookbook.ingredients.models import Category, Ingredient



class UserType(DjangoObjectType):
    class Meta:
        model = MyUser

class ProfileType(DjangoObjectType):
    class Meta:
        model = MyProfile





class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(ObjectType):

    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    #all_ingredients = graphene.List(IngredientType)

    #def resolve_all_categories(self, info, **kwargs):
    #    return Category.objects.all()

    #def resolve_all_ingredients(self, info, **kwargs):

     #   return Ingredient.objects.select_related('category').all()


    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)

