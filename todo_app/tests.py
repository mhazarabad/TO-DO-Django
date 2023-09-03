from django.test import TestCase
from . import models
from django.contrib.auth.models import User

class BlogTestCase(TestCase):
    def setUp(self):
        user_james=User.objects.create(
            first_name='jsmes',
            username='_test__james',
            password='_'
        )

        user_jscob=User.objects.create(
            first_name='jscob',
            username='_test__jscob',
            password='_'
        )

    def test_create_edit_delete_todo(self):

        user_james=User.objects.get(username='_test__james')
        user_jscob=User.objects.get(username='_test__jscob')


        todo_without_optionals=models.Todo.objects.create(
            name='todo test 1',
            by=user_james
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
            first=todo_without_optionals.by.id, 
            second=user_james.id,
            msg='TEST 5: todo by must be {} but it is {}'.format(user_james.id,todo_without_optionals.by.id)
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
            by=user_jscob,
            description=description
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
            first=todo_with_description.by.id, 
            second=user_jscob.id,
            msg='TEST 13: todo by must be {} but it is {}'.format(user_jscob.id,todo_with_description.by.id)
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
            by=user_james,
            status='2',
            description=description,
            due_date=due_date
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
            first=todo_with_due_date.by.id, 
            second=user_james.id,
            msg='TEST 21: todo by must be {} but it is {}'.format(user_james.id,todo_with_due_date.by.id)
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
            by=user_jscob,
            status='3',
            description=description,
            start_date=start_date
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
            first=todo_with_start_date.by.id, 
            second=user_jscob.id,
            msg='TEST 29: todo by must be {} but it is {}'.format(user_jscob.id,todo_with_start_date.by.id)
            )

        self.assertEqual(
            first=todo_with_start_date.description, 
            second=description, 
            msg='TEST 30: todo description must be {} but it is {}'.format(description,todo_with_start_date.description)
            )
        
        self.assertEqual(
            first=todo_with_start_date.due_date, 
            second=due_date,
            msg='TEST 31: todo due date must be {} but it is {}'.format(due_date, todo_with_start_date.due_date)
            )
        
        self.assertEqual(
            first=todo_with_start_date.start_date, 
            second=None, 
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
        
        self.assertGreater(
            first=todo_without_optionals.last_update_datetime, 
            second=todo_without_optionals.creation_datetime, 
            msg='TEST 34: todo creation_datetime must be greater than {} but it is {}'.format(todo_without_optionals.last_update_datetime, todo_without_optionals.creation_datetime)
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
        user_jscob=User.objects.get(username='_test__jscob')
        description='some text to test description'
        from django.utils import timezone
        from datetime import timedelta
        date_future_1=timezone.now()+timedelta(days=5)
        date_future_2=timezone.now()+timedelta(days=10)
        date_now=timezone.now()
        date_past_1=timezone.now()-timedelta(days=10)
        date_past_2=timezone.now()-timedelta(days=15)

        todo_past=models.Todo.objects.create(
            name='todo test past',
            by=user_jscob,
            description=description,
            start_date=date_past_1,
            due_date=date_past_2
        )

        todo_present=models.Todo.objects.create(
            name='todo test present',
            by=user_jscob,
            description=description,
            start_date=date_now,
            due_date=date_future_1
        )

        todo_future=models.Todo.objects.create(
            name='todo test future',
            by=user_jscob,
            description=description,
            start_date=date_future_1,
            due_date=date_future_2
        )

        #### test sort_todo_by_closer_due_date

        self.assertEqual(
            [todo.id for todo in models.Todo.sort_todo_by_closer_due_date(by=user_jscob)],
            [todo_past.id,todo_present.id,todo_future.id], 
            msg='TEST 46: todo method test {} failed- expected values: {} - returnned values: {}'.format(
                'sort_todo_by_closer_due_date',
                [todo_past.id,todo_present.id,todo_future.id],
                [todo.id for todo in models.Todo.sort_todo_by_closer_due_date(by=user_jscob)])
        )

        #### test sort_todo_by_closer_start_date

        self.assertEqual(
            [todo.id for todo in models.Todo.sort_todo_by_closer_start_date(by=user_jscob)],
            [todo_past.id,todo_present.id,todo_future.id], 
            msg='TEST 47: todo method test {} failed- expected values: {} - returnned values: {}'.format(
                'sort_todo_by_closer_start_date',
                [todo_past.id,todo_present.id,todo_future.id],
                [todo.id for todo in models.Todo.sort_todo_by_closer_start_date(by=user_jscob)])
        )

        #### test sort_todo_by_passed_deadline

        self.assertEqual(
            [todo.id for todo in models.Todo.sort_todo_by_passed_deadline(by=user_jscob)],
            [todo_past.id], 
            msg='TEST 47: todo method test {} failed- expected values: {} - returnned values: {}'.format(
                'sort_todo_by_closer_start_date',
                [todo_past.id],
                [todo.id for todo in models.Todo.sort_todo_by_passed_deadline(by=user_jscob)])
        )

        todo_past.delete()
        todo_present.delete()
        todo_future.delete()

    def test_todo_get_APIs(self):
        user_jscob=User.objects.get(username='_test__jscob')
        description='some text to test description'
        from django.utils import timezone
        from datetime import timedelta
        date_future_1=timezone.now()+timedelta(days=5)
        date_future_2=timezone.now()+timedelta(days=10)
        date_now=timezone.now()
        date_past_1=timezone.now()-timedelta(days=10)
        date_past_2=timezone.now()-timedelta(days=15)

        todo_past=models.Todo.objects.create(
            name='todo test past',
            by=user_jscob,
            description=description,
            start_date=date_past_1,
            due_date=date_past_2
        )

        todo_present=models.Todo.objects.create(
            name='todo test present',
            by=user_jscob,
            description=description,
            start_date=date_now,
            due_date=date_future_1
        )

        todo_future=models.Todo.objects.create(
            name='todo test future',
            by=user_jscob,
            description=description,
            start_date=date_future_1,
            due_date=date_future_2
        )

        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1"})
        url='/todo/{}'.format(todo_present.id)
        response = client.get(path=url)

        self.assertEqual(
            first=response.status_code,
            second=200,
            msg='TEST 46: status code for get request must be {} but is {} for url {}'.format(
                200,
                response.status_code,
                url
            )
        )

        self.assertEqual(
            first=response.json(),
            second=dict(todo_present),
            msg="TEST 48: todo get detail is wrong."
        )

    def test_todo_post_APIs(self):
        pass

    def test_todo_put_APIs(self):
        pass

    def test_todo_delete_APIs(self):
        pass

