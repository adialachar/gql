from rest_framework import serializers
from .models import MyUser, Profile
from .email import send_application_email
import jwt
from django.http import JsonResponse

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =  ('first_name', 'last_name', 'school', 'level_of_study', 'graduation_year', 'major', \
     'gender', 'gender_other', 'race', 'race_other', 'phone_number', 'date_of_birth', 'shirt_size', 'dietary_restrictions', 'linkedin', \
     'github', 'resume', 'conduct_box', 'share_box')


    def create(self, user, profile_data):
        Profile.objects.create(user, profile_data)
        return None




class MyUserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()


    class Meta:
        model = MyUser
        fields = ('email', 'password', 'profile')


    def create(self, validated_data):

        print("I HAVE ENETERED BOIIIIIIIIIIIIIIII")

        u = MyUser.objects.create_user(validated_data.get('email'), validated_data.get('password'))
        profile_data = validated_data.pop('profile')
        Profile.objects.create_profile(user=u, profile_data=profile_data)
        send_application_email(validated_data.get('email'))

        token = jwt.encode({'user':validated_data.get('email')}, "SECRET_KEY")
        #try:
        #    decToken = jwt.decode(token, "SECRET_KEY")
        #except:
        #    return JsonResponse({"ur mom": "gei"})
        #token = token.decode('utf-8')
        #return JsonResponse({"token":token})
        return u
