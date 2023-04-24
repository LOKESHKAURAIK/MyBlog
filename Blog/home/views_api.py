from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Profile
from .helpers import *

class LoginView(APIView):

    def post(self, request):
        response = {}                       
        response['status'] = 500
        response['message'] = 'Somthing went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username is not found'
                raise Exception('username is not found')

            if data.get('password') is None:
                response['message'] = 'password is not found'
                raise Exception('password is not found')

            check_user = User.objects.filter(
                username=data.get('username')).first()
            if check_user is None:
                response['message'] = 'invalid username, user not found'
                raise Exception('invalid username not found')
            
            if not Profile.objects.filter(user = check_user).first().is_verified:
                response['message'] = 'Your profile is not verified'
                raise Exception('Profile not verified')

        

            user_obj = authenticate( email = data.get('username'), username=data.get(
                'username'), password=data.get('password'))

            if user_obj:
                login(request, user_obj)  # login from here
                response['status'] = 200
                response['message'] = 'Welcome User'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')

        except Exception as e:
            print(e)
        return Response(response)


# LoginView = LoginView.as_view()   # for class based function 


class RegisterView(APIView):

    def post(self, request):
        response = {}                       #empty dictionary
        response['status'] = 500
        response['message'] = 'Somthing went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username is not found'
                raise Exception('username is not found')

            if data.get('password') is None:
                response['message'] = 'password is not found'
                raise Exception('password is not found')

            check_user = User.objects.filter(
                username=data.get('username')).first()
            if check_user:
                response['message'] = 'username already taken'
                raise Exception('username already taken')

            user_obj = User.objects.create(email = data.get('username'), username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()

            token = generate_random_string(20)
            print(token)
            Profile.objects.create(user = user_obj, token = token)

            # send_mail_to_user(token, data.get('username'))


            response['status'] = 200
            response['message'] = 'User created'
        except Exception as e:
            print(e)
        return Response(response)



