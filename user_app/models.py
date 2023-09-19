from django.db import models

class UserToken(models.Model):
    from uuid import uuid4
    from django.contrib.auth.models import User
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    token=models.UUIDField(primary_key=True,default=uuid4)
    login_datetime=models.DateTimeField(auto_now_add=True)
    logout_datetime=models.DateTimeField(blank=True,null=True)
    is_valid=models.BooleanField()

    def save(self,*args,**kwargs):
        from django.utils import timezone

        if self.is_valid == False and self.logout_datetime==None:
            self.logout_datetime=timezone.now()

        if self.logout_datetime!=None:
            self.is_valid=False

        if self.login_datetime==None:# considered as new object creation
            try:
                self._disable_previous_valid_token(user=self.user)
            except Exception as e:
                raise Exception('error in disabling previous tokens')

        return super().save(*args,**kwargs)
    
    @classmethod
    def get_user_from_username_password(cls,user_username:str,user_password:str)-> User:
        from django.contrib.auth.models import User
        from django.core.exceptions import ObjectDoesNotExist
        try:
            user=User.objects.get(username=user_username)
        except ObjectDoesNotExist:
            return None
        except Exception as e:
            raise Exception('error in searching for user')
        if user.check_password(raw_password=user_password):
            return user
        return None
    
    @classmethod
    def _disable_previous_valid_token(cls,user:User) -> None:
        from django.utils import timezone
        try:
            previous_valid_tokens=cls.objects.filter(user=user,is_valid=True)
            if len(previous_valid_tokens)>0:
                previous_valid_tokens.update(
                    logout_datetime=timezone.now(),
                    is_valid=False
                )
        except Exception as e:
            raise Exception('error in disableing old tokens')

    @classmethod
    def get_new_token(cls,user:User) -> str:     
        try:
            return str(cls.objects.create(user=user,is_valid=True).token)
        except Exception as e:
            raise Exception("error in generating new token: {}".format(str(e)))
        
    @classmethod
    def logout_token(cls,user:user) -> None:
        cls._disable_previous_valid_token(user=user)
    
    @classmethod
    def get_user_from_token(cls,token:str) -> User:
        from django.core.exceptions import ObjectDoesNotExist
        try:
            return cls.objects.get(token=str(token),is_valid=True,logout_datetime__isnull=True).user
        except ObjectDoesNotExist:
            return None
        except Exception as e:
            raise Exception('error in geting user from token: {}'.format(str(e)))