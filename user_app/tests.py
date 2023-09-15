from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username='user_1',
            password='_',
            first_name='user 1',
            last_name='user 1 last name'
        )

        User.objects.create(
            username='user_2',
            password='_',
            first_name='user 2',
            last_name='user 2 last name'
        )

    def test_user_API_post(self):

        create_user_data = {
            'username': 'new user',  # required field, unique
            'password': '_',  # requierd
            'first_name': 'new user first name',  # optional
            'last_name': 'new user last name',  # optional
        }

        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1"})

        post_url = '/user/'
        post_user_response = client.post(
            path=post_url, data=create_user_data, content_type='application/json')

        self.assertEqual(
            first=post_user_response.status_code,
            second=200,
            msg='status code for post method with API should be 200 but is {}'.format(
                post_user_response.status_code)
        )

        response_data = post_user_response.json()

        self.assertEqual(
            first=response_data.get('data',{}).get('username'),
            second=create_user_data['username'],
            msg='response message error, response username must be {} but is {}'.format(
                create_user_data['username'], response_data.get('data',{}).get('username'))
        )

        self.assertEqual(
            first=response_data.get('data',{}).get('first_name'),
            second=create_user_data['first_name'],
            msg='response message error, response first_name must be {} but is {}'.format(
                create_user_data['first_name'], response_data.get('data',{}).get('first_name'))
        )

        self.assertEqual(
            first=response_data.get('data',{}).get('last_name'),
            second=create_user_data['last_name'],
            msg='response message error, response last_name must be {} but is {}'.format(
                create_user_data['last_name'], response_data.get('data',{}).get('last_name'))
        )

        self.assertEqual(
            first=response_data.get('data',{}).get('password'),
            second=None,
            msg='response should not return password but returns {}'.format(
                response_data.get('data',{}).get('password'))
        )

    def test_user_API_get(self):
        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1"})

        user_1=User.objects.get(username='user_1')

        get_user = '/user/{}/'.format(user_1.username)
        get_user_response = client.get(path=get_user)

        self.assertEqual(
            first=get_user_response.status_code,
            second=200,
            msg='status code with get method for url /user/{} should be 200 but is {}'.format(user_1.username,get_user_response.status_code)
        )

        response_data=get_user_response.json()

        self.assertEqual(
            first=response_data.get('data',{}).get('username'),
            second=user_1.username,
            msg='error in response get- username must be {} but is {}'.format(user_1.username,response_data.get('data',{}).get('username'))
        )

        self.assertEqual(
            first=response_data.get('data',{}).get('first_name'),
            second=user_1.first_name,
            msg='error in response get- first_name must be {} but is {}'.format(user_1.first_name,response_data.get('data',{}).get('first_name'))
        )

        self.assertEqual(
            first=response_data.get('data',{}).get('last_name'),
            second=user_1.last_name,
            msg='error in response get- last_name must be {} but is {}'.format(user_1.last_name,response_data.get('data',{}).get('last_name'))
        )
        
    def test_user_API_put(self):
        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1"})

        edit_user_data = {
            'id': 34568, # this item should not be changed
            'username': 'edited_username', 
            'last_name': 'new_last_name'
        }

        user_1=User.objects.get(username='user_1')

        put_url = '/user/{}/'.format(user_1.username)
        put_url_response = client.put(
            path=put_url, data=edit_user_data, content_type='application/json')

        

        self.assertEqual(
            first=put_url_response.status_code,
            second=200,
            msg='status code with put method for url /user/{} should be 200 but is {}'.format(user_1.username,put_url_response.status_code)
        )

        response_data=put_url_response.json()

        self.assertEqual(
            first=response_data.get('data',{}).get('username'),
            second=edit_user_data['username'],
            msg='error in response put- username must be {} but is {}'.format(edit_user_data['username'],response_data.get('data',{}).get('username'))
        )

        self.assertEqual(
            first=response_data.get('data',{}).get('first_name'),
            second=user_1.first_name,
            msg='error in response put- first_name must be {} but is {}'.format(user_1.first_name,response_data.get('data',{}).get('first_name'))
        )

        self.assertEqual(
            first=response_data.get('data',{}).get('last_name'),
            second=edit_user_data['last_name'],
            msg='error in response put- last_name must be {} but is {}'.format(edit_user_data['last_name'],response_data.get('data',{}).get('last_name'))
        )

        self.assertNotEqual(
            first=response_data.get('data',{}).get('id'),
            second=edit_user_data['id'],
            msg='error in response put- id for user should not be change'
        )

    def test_user_API_delete(self):
        from django.test import Client
        client = Client(headers={"user-agent": "curl/7.79.1"})

        user_2=User.objects.get(username='user_2')

        delete_url = '/user/{}/'.format(user_2.username)
        delete_url_response = client.delete(
            path=delete_url, content_type='application/json')
        
        self.assertEqual(
            first=delete_url_response.status_code,
            second=200,
            msg='status code with delete method for url /user/{} should be 200 but is {}'.format(user_2.username,delete_url_response.status_code)
        )

        self.assertEqual(
            first=User.objects.filter(username=user_2.username).exists(),
            second=False,
            msg='delete request did not delete the object'
        )
