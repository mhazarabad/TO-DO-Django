from django.test import TestCase
from . import models
from django.contrib.auth.models import User

class TodoTestCase(TestCase):
    def setUp(self):
        user_1=User.objects.create(
            username='user_1',
            first_name='user 1 first name',
            last_name='user 1 last name',
        )

        user_5=User.objects.create(
            username='user_5',
            first_name='user 5 first name',
            last_name='user 5 last name',
        )

    def test_create_edit_delete_todo(self):

        user_1=User.objects.get(username='user_1')
        user_5=User.objects.get(username='user_5')

        todo_without_optionals=models.Todo.objects.create(
            name='todo test 1',
            by=user_5
            )
        
        self.assertEqual(
            first=todo_without_optionals.status, 
            second='1', 
            msg='TEST 1: status for this todo must be {} but it is {}'.format('1',todo_without_optionals.status)
            )
        
        self.assertNotEqual(
            first=todo_without_optionals.id, 
            second=None, 
            msg='TEST 2: id for this todo must be {} but it is {}'.format(todo_without_optionals.id, None)
            )
        
        self.assertNotEqual(
            first=todo_without_optionals.last_update_datetime, 
            second=None, 
            msg='TEST 3: last update datetime must be filled automatically but it is None'
            )
        
        self.assertNotEqual(
            first=todo_without_optionals.creation_datetime, 
            second=None, 
            msg='TEST 4: creation date time must be filled automatically but it is None'
            )
        
        self.assertEqual(
            first=todo_without_optionals.description, 
            second=None, 
            msg='TEST 6: todo description must be {} but it is {}'.format(None,todo_without_optionals.description)
            )
        
        self.assertEqual(
            first=todo_without_optionals.due_date, 
            second=None,
            msg='TEST 7: todo due date must be {} but it is {}'.format(None, todo_without_optionals.due_date)
            )
        
        self.assertEqual(
            first=todo_without_optionals.start_date, 
            second=None, 
            msg='TEST 8: todo start date must be {} but it is {}'.format(None, todo_without_optionals.start_date)
            )


        description='some text to test description'

        todo_with_description=models.Todo.objects.create(
            name='todo test 2',
            description=description,
            by=user_5
        )

        self.assertEqual(
            first=todo_with_description.status, 
            second='1', 
            msg='TEST 9: status for this todo must be {} but it is {}'.format('1',todo_with_description.status)
            )
                
        self.assertNotEqual(
            first=todo_with_description.id, 
            second=None, 
            msg='TEST 10: id for this todo must be {} but it is {}'.format(todo_with_description.id, None)
            )
        
        self.assertNotEqual(
            first=todo_with_description.last_update_datetime, 
            second=None, 
            msg='TEST 11: last update datetime must be filled automatically but it is None'
            )
        
        self.assertNotEqual(
            first=todo_with_description.creation_datetime, 
            second=None, 
            msg='TEST 12: creation date time must be filled automatically but it is None'
            )
        
        self.assertEqual(
            first=todo_with_description.description, 
            second=description, 
            msg='TEST 14: todo description must be {} but it is {}'.format(description,todo_with_description.description)
            )
        
        self.assertEqual(
            first=todo_with_description.due_date, 
            second=None,
            msg='TEST 15: todo due date must be {} but it is {}'.format(None, todo_with_description.due_date)
            )
        
        self.assertEqual(
            first=todo_with_description.start_date, 
            second=None, 
            msg='TEST 16: todo start date must be {} but it is {}'.format(None, todo_with_description.start_date)
            )


        from django.utils import timezone
        due_date=timezone.now()
        
        todo_with_due_date=models.Todo.objects.create(
            name='todo test 3',
            status='2',
            description=description,
            due_date=due_date,
            by=user_5
        )

        self.assertEqual(
            first=todo_with_due_date.status, 
            second='2', 
            msg='TEST 17: status for this todo must be {} but it is {}'.format('2',todo_with_due_date.status)
            )
        
        self.assertNotEqual(
            first=todo_with_due_date.id, 
            second=None, 
            msg='TEST 18: id for this todo must be {} but it is {}'.format(todo_with_due_date.id, None)
            )
        
        self.assertNotEqual(
            first=todo_with_due_date.last_update_datetime, 
            second=None, 
            msg='TEST 19: last update datetime must be filled automatically but it is None'
            )
        
        self.assertNotEqual(
            first=todo_with_due_date.creation_datetime, 
            second=None, 
            msg='TEST 20: creation date time must be filled automatically but it is None'
            )

        self.assertEqual(
            first=todo_with_due_date.description, 
            second=description, 
            msg='TEST 22: todo description must be {} but it is {}'.format(description,todo_with_due_date.description)
            )
        
        self.assertEqual(
            first=todo_with_due_date.due_date, 
            second=due_date,
            msg='TEST 23: todo due date must be {} but it is {}'.format(due_date, todo_with_due_date.due_date)
            )
        
        self.assertEqual(
            first=todo_with_due_date.start_date, 
            second=None, 
            msg='TEST 24: todo start date must be {} but it is {}'.format(None, todo_with_due_date.start_date)
            )


        start_date=timezone.now()

        todo_with_start_date=models.Todo.objects.create(
            name='todo test 4',
            status='3',
            description=description,
            start_date=start_date,
            by=user_5
        )

        self.assertEqual(
            first=todo_with_start_date.status, 
            second='3', 
            msg='TEST 25: status for this todo must be {} but it is {}'.format('3',todo_with_start_date.status)
            )
        
        self.assertNotEqual(
            first=todo_with_start_date.id, 
            second=None, 
            msg='TEST 26: id for this todo must be {} but it is {}'.format(todo_with_start_date.id, None)
            )
        
        self.assertNotEqual(
            first=todo_with_start_date.last_update_datetime, 
            second=None, 
            msg='TEST 27: last update datetime must be filled automatically but it is None'
            )
        
        self.assertNotEqual(
            first=todo_with_start_date.creation_datetime, 
            second=None, 
            msg='TEST 28: creation date time must be filled automatically but it is None'
            )

        self.assertEqual(
            first=todo_with_start_date.description, 
            second=description, 
            msg='TEST 30: todo description must be {} but it is {}'.format(description,todo_with_start_date.description)
            )
        
        self.assertEqual(
            first=todo_with_start_date.due_date, 
            second=None,
            msg='TEST 31: todo due date must be {} but it is {}'.format(None, todo_with_start_date.due_date)
            )
        
        self.assertEqual(
            first=todo_with_start_date.start_date, 
            second=start_date, 
            msg='TEST 32: todo start date must be {} but it is {}'.format(None, todo_with_start_date.start_date)
            )


        #### testing editing objectts
        # instruction:
        # 1- set new parameter
        # 2- save
        # 3- check for change on db
        # 4- check for change on automated tasks

        todo_without_optionals.status='2'
        todo_without_optionals.save()

        self.assertEqual(
            first=todo_without_optionals.start_date, 
            second=None, 
            msg='TEST 33: todo status must be {} but it is {}'.format('2', todo_without_optionals.status)
            )

        todo_with_description.status='3'
        todo_with_description.save()

        self.assertEqual(
            first=todo_with_description.status, 
            second='3', 
            msg='TEST 35: todo status must be {} but it is {}'.format('3', todo_with_description.status)
            )

        new_start_date=timezone.now()
        todo_with_start_date.start_date=new_start_date
        todo_with_start_date.save()

        self.assertEqual(
            first=todo_with_start_date.start_date, 
            second=new_start_date, 
            msg='TEST 36: todo start date must be {} but it is {}'.format(new_start_date, todo_with_start_date.start_date)
            )


        new_due_date=timezone.now()
        todo_with_due_date.due_date=new_due_date
        todo_with_due_date.save()

        self.assertEqual(
            first=todo_with_due_date.due_date, 
            second=new_due_date, 
            msg='TEST 37: todo due date must be {} but it is {}'.format(new_due_date, todo_with_due_date.due_date)
            )

        user_1=User.objects.get(username='user_1')
        todo_with_description.assign=user_1
        todo_with_description.save()
        self.assertEqual(
            first=todo_with_description.export_to_response['assign'],
            second=models.Todo.export_user_to_response(user_object=user_1),
            msg='TEST 67: editing todo - assign a user to todo failed'
        )

        #### testing deleting objectts
        # instruction:
        # 1- get object id
        # 2- check object exist -> True
        # 3- delete object
        # 4- check object exist -> False

        todo_with_due_date_id=todo_with_due_date.id
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_with_due_date_id).exists(), 
            second=True, 
            msg='TEST 38: pre check for deleting an object failed - object not found'
            )
        todo_with_due_date.delete()
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_with_due_date_id).exists(), 
            second=False, 
            msg='TEST 39: after check for deleting an object failed - object still exist'
            )
        

        todo_with_start_date_id=todo_with_start_date.id
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_with_start_date_id).exists(), 
            second=True, 
            msg='TEST 40: pre check for deleting an object failed - object not found'
            )
        todo_with_start_date.delete()
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_with_start_date_id).exists(), 
            second=False, 
            msg='TEST 41: after check for deleting an object failed - object still exist'
            )


        todo_with_description_id=todo_with_description.id
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_with_description_id).exists(), 
            second=True, 
            msg='TEST 42: pre check for deleting an object failed - object not found'
            )
        todo_with_description.delete()
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_with_description_id).exists(), 
            second=False, 
            msg='TEST 43: after check for deleting an object failed - object still exist'
            )


        todo_without_optionals_id=todo_without_optionals.id
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_without_optionals_id).exists(), 
            second=True, 
            msg='TEST 44: pre check for deleting an object failed - object not found'
            )
        todo_without_optionals.delete()
        self.assertEqual(
            first=models.Todo.objects.filter(id=todo_without_optionals_id).exists(), 
            second=False, 
            msg='TEST 45: after check for deleting an object failed - object still exist'
            )

    def test_todo_methods(self):
        description='some text to test description'
        from django.utils import timezone
        from datetime import timedelta
        date_future_1=timezone.now()+timedelta(days=5)
        date_future_2=timezone.now()+timedelta(days=10)
        date_now=timezone.now()
        date_past_1=timezone.now()-timedelta(days=10)
        date_past_2=timezone.now()-timedelta(days=15)

        user_1=User.objects.get(username='user_1')
        user_5=User.objects.get(username='user_5')

        todo_past=models.Todo.objects.create(
            name='todo test past',
            description=description,
            start_date=date_past_1,
            due_date=date_past_2,
            by=user_5
        )

        todo_present=models.Todo.objects.create(
            name='todo test present',
            description=description,
            start_date=date_now,
            due_date=date_future_1,
            by=user_5
        )

        todo_future=models.Todo.objects.create(
            name='todo test future',
            description=description,
            start_date=date_future_1,
            due_date=date_future_2,
            by=user_5
        )

        #### test sort_todo_by_closer_due_date

        self.assertEqual(
            [todo.id for todo in models.Todo.sort_todo_by_closer_due_date()],
            [todo_past.id,todo_present.id,todo_future.id], 
            msg='TEST 46: todo method test {} failed- expected values: {} - returnned values: {}'.format(
                'sort_todo_by_closer_due_date',
                [todo_past.id,todo_present.id,todo_future.id],
                [todo.id for todo in models.Todo.sort_todo_by_closer_due_date()])
        )

        #### test sort_todo_by_closer_start_date

        self.assertEqual(
            [todo.id for todo in models.Todo.sort_todo_by_closer_start_date()],
            [todo_past.id,todo_present.id,todo_future.id], 
            msg='TEST 47: todo method test {} failed- expected values: {} - returnned values: {}'.format(
                'sort_todo_by_closer_start_date',
                [todo_past.id,todo_present.id,todo_future.id],
                [todo.id for todo in models.Todo.sort_todo_by_closer_start_date()])
        )

        #### test sort_todo_by_passed_deadline

        self.assertEqual(
            [todo.id for todo in models.Todo.sort_todo_by_passed_deadline()],
            [todo_past.id], 
            msg='TEST 48: todo method test {} failed- expected values: {} - returnned values: {}'.format(
                'sort_todo_by_closer_start_date',
                [todo_past.id],
                [todo.id for todo in models.Todo.sort_todo_by_passed_deadline()])
        )

        todo_past.delete()
        todo_present.delete()
        todo_future.delete()

    def test_todo_get_APIs(self):
        description='some text to test description'
        from django.utils import timezone
        from datetime import timedelta
        date_future_1=timezone.now()+timedelta(days=5)
        date_future_2=timezone.now()+timedelta(days=10)
        date_now=timezone.now()
        date_past_1=timezone.now()-timedelta(days=10)
        date_past_2=timezone.now()-timedelta(days=15)

        user_5=User.objects.get(username='user_5')

        from user_app.models import UserToken
        token_user_5=str(UserToken.objects.create(user=user_5,is_valid=True).token)
        

        todo_past=models.Todo.objects.create(
            name='todo test past',
            description=description,
            start_date=date_past_1,
            due_date=date_past_2,
            by=user_5
            )

        todo_present=models.Todo.objects.create(
            name='todo test present',
            description=description,
            start_date=date_now,
            due_date=date_future_1,
            by=user_5
            )

        todo_future=models.Todo.objects.create(
            name='todo test future',
            description=description,
            start_date=date_future_1,
            due_date=date_future_2,
            by=user_5
            )


        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1","Authorization":"Bearer {}".format(token_user_5)})


        url_present='/todo/{}/'.format(todo_present.id)
        response_present = client.get(path=url_present)

        self.assertEqual(
            first=response_present.status_code,
            second=200,
            msg='TEST 49: status code for get request must be {} but is {} for url {}'.format(
                200,
                response_present.status_code,
                url_present
            )
        )
        
        self.assertEqual(
            first=response_present.json()['data'],
            second=todo_present.export_to_response,
            msg="TEST 50: todo get detail is wrong."
        )


        url_past='/todo/{}/'.format(todo_past.id)
        response_past = client.get(path=url_past)

        self.assertEqual(
            first=response_past.status_code,
            second=200,
            msg='TEST 51: status code for get request must be {} but is {} for url {}'.format(
                200,
                response_past.status_code,
                url_past
            )
        )

        self.assertEqual(
            first=response_past.json()['data'],
            second=todo_past.export_to_response,
            msg="TEST 52: todo get detail is wrong."
        )


        url_future='/todo/{}/'.format(todo_future.id)
        response_future = client.get(path=url_future)

        self.assertEqual(
            first=response_future.status_code,
            second=200,
            msg='TEST 53: status code for get request must be {} but is {} for url {}'.format(
                200,
                response_future.status_code,
                url_future
            )
        )

        self.assertEqual(
            first=response_future.json()['data'],
            second=todo_future.export_to_response,
            msg="TEST 54: todo get detail is wrong."
        )

        todo_past.delete()
        todo_present.delete()
        todo_future.delete()

    def test_todo_post_APIs(self):

        description='some text to test description'
        from django.utils import timezone
        from datetime import timedelta
        date_future=timezone.now()+timedelta(days=5)
        date_past=timezone.now()-timedelta(days=10)

        user_5=User.objects.get(username='user_5')
        from user_app.models import UserToken
        token_user_5=str(UserToken.objects.create(user=user_5,is_valid=True).token)


        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1","Authorization":"Bearer {}".format(token_user_5)})

        data_present={
            "name":"create Todo in POST API",
            "description":description,
            "start_date":"{} {}".format(date_past.strftime("%d/%m/%Y %H:%M:%S"),"UTC"),
            "due_date":"{} {}".format(date_future.strftime("%d/%m/%Y %H:%M:%S"),"UTC"),
        }

        post_url='/todo/'
        response_present = client.post(path=post_url,data=data_present,content_type='application/json',)
        self.assertEqual(
            first=response_present.status_code,
            second=200,
            msg='TEST 55: status code for post request must be {} but is {} for url {}'.format(
                200,
                response_present.status_code,
                post_url
            )
        )

        response_data=response_present.json()['data']

        self.assertEqual(
            first=response_data.get('name'),
            second=data_present['name'],
            msg='TEST 56: posted data is not equal to saved data with field {}'.format('name')
        )

        self.assertEqual(
            first=response_data.get('description'),
            second=data_present['description'],
            msg='TEST 57: posted data is not equal to saved data with field {}'.format('description')
        )

        self.assertEqual(
            first=response_data.get('start_date'),
            second=data_present['start_date'],
            msg='TEST 58: posted data is not equal to saved data with field {}'.format('start_date')
        )

        self.assertEqual(
            first=response_data.get('due_date'),
            second=data_present['due_date'],
            msg='TEST 59: posted data is not equal to saved data with field {}'.format('due_date')
        )

    def test_todo_put_APIs(self):
        new_description='some text to test description 2'
        from django.utils import timezone
        from datetime import timedelta
        new_date_future=timezone.now()+timedelta(days=5)
        new_date_past=timezone.now()-timedelta(days=10)
        description='some text to test description'
        date_past_1=timezone.now()-timedelta(days=10)
        date_past_2=timezone.now()-timedelta(days=15)

        user_5=User.objects.get(username='user_5')
        from user_app.models import UserToken
        token_user_5=str(UserToken.objects.create(user=user_5,is_valid=True).token)

        todo_past=models.Todo.objects.create(
            name='Create todo to test put',
            description=description,
            start_date=date_past_1,
            due_date=date_past_2,
            by=user_5
        )

        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1","Authorization":"Bearer {}".format(token_user_5)})

        data_present={
            "description":new_description,
            "start_date":"{} {}".format(new_date_future.strftime("%d/%m/%Y %H:%M:%S"),"UTC"),
            "due_date":"{} {}".format(new_date_past.strftime("%d/%m/%Y %H:%M:%S"),"UTC"),
        }

        todo=models.Todo.objects.get(name="Create todo to test put")

        put_url='/todo/{}/'.format(todo.id)
        response_present = client.put(path=put_url,data=data_present,content_type='application/json',)

        self.assertEqual(
            first=response_present.status_code,
            second=200,
            msg='TEST 61: status code for put request must be {} but is {} for url {}'.format(
                200,
                response_present.status_code,
                put_url
            )
        )

        response_data=response_present.json()['data']

        self.assertEqual(
            first=response_data.get('description'),
            second=data_present['description'],
            msg='TEST 62: edited data is not equal to saved data with field {}'.format('description')
        )

        self.assertEqual(
            first=response_data.get('start_date'),
            second=data_present['start_date'],
            msg='TEST 63: edited data is not equal to saved data with field {}'.format('start_date')
        )

        self.assertEqual(
            first=response_data.get('due_date'),
            second=data_present['due_date'],
            msg='TEST 64: edited data is not equal to saved data with field {}'.format('due_date')
        )

    def test_todo_delete_APIs(self):
        user_5=User.objects.get(username='user_5')
        from user_app.models import UserToken
        token_user_5=str(UserToken.objects.create(user=user_5,is_valid=True).token)


        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1","Authorization":"Bearer {}".format(token_user_5)})

        from django.utils import timezone
        from datetime import timedelta
        description='some text to test description'
        date_past_1=timezone.now()-timedelta(days=10)
        date_past_2=timezone.now()-timedelta(days=15)

        todo_past=models.Todo.objects.create(
            name='Create todo to test delete',
            description=description,
            start_date=date_past_1,
            due_date=date_past_2,
            by=user_5
        )

        todo=models.Todo.objects.get(name="Create todo to test delete")

        delete_url='/todo/{}/'.format(todo.id)
        response_present = client.put(path=delete_url)

        self.assertEqual(
            first=response_present.status_code,
            second=200,
            msg='TEST 65: status code for delete request must be {} but is {} for url {}'.format(
                200,
                response_present.status_code,
                delete_url
            )
        )

        self.assertEqual(
            first=models.Todo.objects.filter(name="create Todo in POST API").exists(),
            second=False,
            msg='TEST 66: Delete request did not delete the object'
        )

