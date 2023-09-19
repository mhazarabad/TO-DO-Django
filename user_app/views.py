MINIMUM_USER_USERNAME_LENGTH=4
MINIMUM_USER_PASSWORD_LENGTH=8

def Get_Json_Data_From_API(request,keyword,on_error_value,part='body'):
    from json import loads as From_Json
    try:
        if part=='body':
            variable=From_Json(request.body.decode("utf-8"))[keyword]
        else:
            variable=request.headers[keyword]
    except:
        variable=on_error_value
    return variable

def User_Manager(request,user_username:str=None):
    MINIMUM_USER_USERNAME_LENGTH=1
    from django.http.response import JsonResponse
    from django.contrib.auth.models import User
    from django.core.exceptions import ObjectDoesNotExist
    match (request.method, user_username):
        case ('GET',_):
            if not user_username:
                return JsonResponse(data={"description":"user_username not received"},status=400)
            
            try:
                user=User.objects.get(username=user_username)
                user_response_data={
                    "id":user.pk,
                    "username":user.username,
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    }
                return JsonResponse(data={"description":"ok","data":user_response_data},status=200)
            except ObjectDoesNotExist:
                return JsonResponse(data={"description":"user not found"},status=404)
            except Exception as e:
                return JsonResponse(data={"description":"Error in finding user: {}".format(str(e))},status=500)
        case ('POST',None):
            new_user_username=Get_Json_Data_From_API(request=request,keyword='username',on_error_value=None)
            new_user_first_name=Get_Json_Data_From_API(request=request,keyword='first_name',on_error_value=None)
            new_user_last_name=Get_Json_Data_From_API(request=request,keyword='last_name',on_error_value=None)
            new_user_password=Get_Json_Data_From_API(request=request,keyword='password',on_error_value=None)

            if new_user_username == None:
                return JsonResponse(data={"description":"username can not be null"},status=400)
            
            new_user_username=str(new_user_username)
            if len(new_user_username)<MINIMUM_USER_USERNAME_LENGTH:
                return JsonResponse(data={"description":"username length can not be less than {}".format(MINIMUM_USER_USERNAME_LENGTH)},status=400)
            
            if new_user_password == None:
                return JsonResponse(data={"description":"password can not be null"},status=400)
            
            try:
                user=User.objects.get(username=new_user_username)
                return JsonResponse(data={"description":"username is already taken"},status=400)
            except ObjectDoesNotExist:
                pass
            except Exception as e:
                return JsonResponse(data={"description":"Error in checking duplicate username: {}".format(str(e))},status=500)
            
            if new_user_first_name:
                new_user_first_name=str(new_user_first_name)
                new_user_first_name=new_user_first_name if len(new_user_first_name)>0 else None

            if new_user_last_name:
                new_user_last_name=str(new_user_last_name)
                new_user_last_name=new_user_last_name if len(new_user_last_name)>0 else None


            from django.contrib.auth.hashers import make_password
            try:
                new_user=User.objects.create(
                    username=new_user_username,
                    first_name=new_user_first_name,
                    last_name=new_user_last_name,
                    password=make_password(new_user_password),
                )
                user_response_data={
                    "id":new_user.pk,
                    "username":new_user.username,
                    "first_name":new_user.first_name,
                    "last_name":new_user.last_name,
                    }
                return JsonResponse(data={"description":"ok","data":user_response_data},status=200)
            except Exception as e:
                return JsonResponse(data={"description":"Error in saving user: {}".format(str(e))},status=500)
        case ('PUT',_):
            if user_username==None:
                return JsonResponse(data={"description":"username can not be null for put requests"},status=400)
            if len(user_username)<MINIMUM_USER_USERNAME_LENGTH:
                return JsonResponse(data={"description":"username length can not be less than {}".format(MINIMUM_USER_USERNAME_LENGTH)},status=400)
            
            user_new_username=Get_Json_Data_From_API(request=request,keyword='username',on_error_value=None)
            user_new_first_name=Get_Json_Data_From_API(request=request,keyword='first_name',on_error_value=None)
            user_new_last_name=Get_Json_Data_From_API(request=request,keyword='last_name',on_error_value=None)
            user_new_password=Get_Json_Data_From_API(request=request,keyword='password',on_error_value=None)

            try:
                user=User.objects.get(username=user_username)
            except ObjectDoesNotExist:
                return JsonResponse(data={"description":"user not found"},status=404)
            except Exception as e:
                return JsonResponse(data={"description":"error in finding user: {}".format(str(e))},status=500)

            if user_new_username!=None:
                user_new_username=str(user_new_username)
                if len(user_new_username)<MINIMUM_USER_USERNAME_LENGTH:
                    return JsonResponse(data={"description":"username length can not be less than {}".format(MINIMUM_USER_USERNAME_LENGTH)},status=400)
                try:
                    User.objects.get(username=user_new_username)
                    return JsonResponse(data={"description":"this username is already exist"},status=400)
                except ObjectDoesNotExist:
                    pass
                except Exception as e:
                    return JsonResponse(data={"description":"error in finding user: {}".format(str(e))},status=500)
                user.username=user_new_username

            if user_new_first_name:
                user_new_first_name=str(user_new_first_name)
                user_new_first_name=user_new_first_name if len(user_new_first_name)>0 else None

            if user_new_last_name:
                user_new_last_name=str(user_new_last_name)
                user_new_last_name=user_new_last_name if len(user_new_last_name)>0 else None

            if user_new_first_name:
                user.first_name=user_new_first_name

            if user_new_last_name:
                user.last_name=user_new_last_name

            if user_new_password:
                from django.contrib.auth.hashers import make_password
                user.password=make_password(user_new_password)

            try:
                user.save()
                user_response_data={
                    "id":user.pk,
                    "username":user.username,
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    }
                return JsonResponse(data={"description":"ok","data":user_response_data},status=200)
            except Exception as e:
                return JsonResponse(data={"description":"error in saving user: {}".format(str(e))},status=500)
        case ('DELETE',_):
            try:
                user=User.objects.get(username=user_username)
            except ObjectDoesNotExist:
                return JsonResponse(data={"description":"user not found"},status=404)
            except Exception as e:
                return JsonResponse(data={"description":"error in finding user: {}".format(str(e))},status=500)
            
            try:
                user.delete()
                return JsonResponse(data={"description":"ok"},status=200)
            except Exception as e:
                return JsonResponse(data={"description":"error in deleting user: {}".format(str(e))},status=500)
        case (_,_):
            return JsonResponse(data={"description":"method not allowed"},status=405)

def Token_Manager(request):
    from django.http.response import JsonResponse
    from django.core.exceptions import ObjectDoesNotExist

    match request.method.lower():
        case 'post':
            user_username=Get_Json_Data_From_API(request=request,keyword='username',on_error_value=None)
            user_password=Get_Json_Data_From_API(request=request,keyword='password',on_error_value=None)

            if user_username:
                user_username=str(user_username)

            if not user_username or len(user_username)<MINIMUM_USER_USERNAME_LENGTH:
                return JsonResponse(data={"description":"username length can not be less than {}".format(MINIMUM_USER_USERNAME_LENGTH)},status=400)

            if user_password:
                user_password=str(user_password)

            if not user_password or len(user_password)<MINIMUM_USER_PASSWORD_LENGTH:
                return JsonResponse(data={"description":"password length can not be less than {}".format(MINIMUM_USER_PASSWORD_LENGTH)},status=400)

            from .models import UserToken

            try:
                user=UserToken.get_user_from_username_password(user_username=user_username,user_password=user_password)
                if user==None:
                    return JsonResponse(data={"description":"username or password is incorrect"},status=403)
            except Exception as e:
                return JsonResponse(data={"description":"error in checking user creadentials: {}".format(str(e))},status=500)
            
            try:
                new_token=UserToken.get_new_token(user=user)
            except Exception as e:
                return JsonResponse(data={"description":"error in creating new token"},status=500)

            return JsonResponse(data={"description":"ok","token":str(new_token)},status=200)
        
        case 'delete':
            user_token=Get_Json_Data_From_API(request=request,keyword='Authorization',on_error_value=None,part='header')

            if user_token:
                user_token=str(user_token)

            user_token=user_token.split(' ')

            if 'bearer' != user_token[0].lower() or len(user_token)!=2:
                return JsonResponse(data={"description":"token format is not valid. valid format is: 'Bearer <your token>'"},status=403)
            
            user_token=str(user_token[1])

            from .models import UserToken
            try:
                user=UserToken.get_user_from_token(token=user_token)
                if user==None:
                    return JsonResponse(data={'description':'invalid token or token is not valid'},status=403)
            except Exception as e:
                return JsonResponse(data={"description":"error in checking token"},status=500)
            
            try:
                UserToken.logout_token(user=user)
            except Exception as e:
                return JsonResponse(data={"description":"error in removing token"},status=500)
            
            return JsonResponse(data={"description":"ok"},status=200)

        case _:
            return JsonResponse(data={"description":"method not allowed"},status=405)
