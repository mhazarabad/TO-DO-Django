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
        self.assertEqual(todo_without_optionals.status, '1')
        self.assertNotEqual(todo_without_optionals.id, None)
        self.assertNotEqual(todo_without_optionals.last_update_datetime, None)
        self.assertNotEqual(todo_without_optionals.creation_datetime, None)
        self.assertEqual(todo_without_optionals.last_update_datetime, todo_without_optionals.creation_datetime)
        self.assertEqual(todo_without_optionals.by, user_james)
        self.assertEqual(todo_without_optionals.description, None)
        self.assertEqual(todo_without_optionals.due_date, None)
        self.assertEqual(todo_without_optionals.start_date, None)


        description='some text to test description'

        todo_with_description=models.Todo.objects.create(
            name='todo test 1',
            by=user_jscob,
            description=description
        )
        self.assertEqual(todo_with_description.status, '1')
        self.assertNotEqual(todo_with_description.id, None)
        self.assertNotEqual(todo_with_description.last_update_datetime, None)
        self.assertNotEqual(todo_with_description.creation_datetime, None)
        self.assertEqual(todo_with_description.by, user_jscob)
        self.assertEqual(todo_with_description.description, description)
        self.assertEqual(todo_with_description.due_date, None)
        self.assertEqual(todo_with_description.start_date, None)


        from django.utils import timezone
        due_date=timezone.now()
        
        todo_with_due_date=models.Todo.objects.create(
            name='todo test 1',
            by=user_james,
            description=description,
            due_date=due_date
        )
        self.assertEqual(todo_with_due_date.status, '1')
        self.assertNotEqual(todo_with_due_date.id, None)
        self.assertNotEqual(todo_with_due_date.last_update_datetime, None)
        self.assertNotEqual(todo_with_due_date.creation_datetime, None)
        self.assertEqual(todo_with_due_date.by, user_james)
        self.assertEqual(todo_with_due_date.description, description)
        self.assertEqual(todo_with_due_date.due_date, due_date)
        self.assertEqual(todo_with_due_date.start_date, None)


        start_date=timezone.now()

        todo_with_start_date=models.Todo.objects.create(
            name='todo test 1',
            by=user_jscob,
            description=description,
            start_date=start_date
        )
        self.assertEqual(todo_with_start_date.status, '1')
        self.assertNotEqual(todo_with_start_date.id, None)
        self.assertNotEqual(todo_with_start_date.last_update_datetime, None)
        self.assertNotEqual(todo_with_start_date.creation_datetime, None)
        self.assertEqual(todo_with_start_date.by, user_jscob)
        self.assertEqual(todo_with_start_date.description, description)
        self.assertEqual(todo_with_start_date.due_date, None)
        self.assertEqual(todo_with_start_date.start_date, start_date)


        #### testing editing objectts
        # instruction:
        # 1- set new parameter
        # 2- save
        # 3- check for change on db
        # 4- check for change on automated tasks

        todo_without_optionals.status='2'
        todo_without_optionals.save()
        self.assertEqual(todo_without_optionals.status, '2')
        self.assertGreater(todo_without_optionals.last_update_datetime, todo_without_optionals.creation_datetime)
        self.assertEqual(todo_without_optionals.creation_datetime, todo_without_optionals.creation_datetime)


        todo_with_description.status='3'
        todo_with_description.save()
        self.assertEqual(todo_with_description.status, '3')
        self.assertGreater(todo_with_description.last_update_datetime, todo_with_description.creation_datetime)
        self.assertEqual(todo_with_description.creation_datetime, todo_with_description.creation_datetime)


        new_start_date=timezone.now()
        todo_with_start_date.start_date=new_start_date
        todo_with_start_date.save()
        self.assertEqual(todo_with_start_date.start_date,new_start_date)
        self.assertGreater(todo_with_start_date.last_update_datetime, todo_with_start_date.creation_datetime)
        self.assertEqual(todo_with_start_date.creation_datetime, todo_with_start_date.creation_datetime)


        new_due_date=timezone.now()
        todo_with_due_date.due_date=new_due_date
        todo_with_due_date.save()
        self.assertEqual(todo_with_due_date.start_date,new_due_date)
        self.assertGreater(todo_with_due_date.last_update_datetime, todo_with_due_date.creation_datetime)
        self.assertEqual(todo_with_due_date.creation_datetime, todo_with_due_date.creation_datetime)


        #### testing deleting objectts
        # instruction:
        # 1- get object id
        # 2- check object exist -> True
        # 3- delete object
        # 4- check object exist -> False

        todo_with_due_date_id=todo_with_due_date.id
        self.assertEqual(models.Todo.objects.filter(id=todo_with_due_date_id).exists(),True)
        todo_with_due_date.delete()
        self.assertEqual(models.Todo.objects.filter(id=todo_with_due_date_id).exists(),False)


        todo_with_start_date_id=todo_with_start_date.id
        self.assertEqual(models.Todo.objects.filter(id=todo_with_start_date_id).exists(),True)
        todo_with_start_date.delete()
        self.assertEqual(models.Todo.objects.filter(id=todo_with_start_date_id).exists(),False)


        todo_with_description_id=todo_with_description.id
        self.assertEqual(models.Todo.objects.filter(id=todo_with_description_id).exists(),True)
        todo_with_description.delete()
        self.assertEqual(models.Todo.objects.filter(id=todo_with_description_id).exists(),False)


        todo_without_optionals_id=todo_without_optionals.id
        self.assertEqual(models.Todo.objects.filter(id=todo_without_optionals_id).exists(),True)
        todo_without_optionals.delete()
        self.assertEqual(models.Todo.objects.filter(id=todo_without_optionals_id).exists(),False)

    def test_todo_methods(self):
        pass

    def test_todo_get_APIs(self):
        pass

    def test_todo_post_APIs(self):
        pass

    def test_todo_put_APIs(self):
        pass

