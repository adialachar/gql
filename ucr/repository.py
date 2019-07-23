from .models import MyUser, Profile


# MyUser.objects.get???
# Profile


def get_user(email):
    return MyUser.objects.get(email=email)

def get_profile(email):
    u = MyUser.objects.get(email=email)

    return Profile.objects.get(user_id = u.pk)
