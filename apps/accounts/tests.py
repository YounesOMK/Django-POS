from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.


class CustomUserTests(TestCase):
    
    def test_new_superuser(self):
        db = get_user_model()
        superuser = db.objects.create_superuser(
            username='test_username',
            email='test@test.com',
            password='test_password',
            first_name='fname',
            last_name='lname',
            phone_number='0600000000',
        )
        
        self.assertEqual(superuser.username, 'test_username')
        self.assertEqual(superuser.email, 'test@test.com')
        self.assertEquals(superuser.check_password('test_password'), True)
        self.assertEqual(superuser.first_name, 'fname')
        self.assertEqual(superuser.last_name, 'lname')
        self.assertEqual(superuser.phone_number, '0600000000')
        
        self.assertEqual(superuser.is_superuser, True)
        self.assertEqual(superuser.is_staff, True)
        self.assertEqual(superuser.is_active, True)
        self.assertEqual(superuser.is_cashier, False)
        
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                username='test_username1',
                email='test1@test.com',
                password='test_password',
                first_name='fname',
                last_name='lname',
                phone_number='0600000000',
                is_superuser=False
            )
            
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                username='test_username2',
                email='test2@test.com',
                password='test_password',
                first_name='fname',
                last_name='lname',
                phone_number='0600000000',
                is_staff=False
            )
            
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                username='test_username3',
                email='test3@test.com',
                password='test_password',
                first_name='fname',
                last_name='lname',
                phone_number='0600000000',
                is_active=False
            )
            
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                username='test_username4',
                email='test4@test.com',
                password='test_password',
                first_name='fname',
                last_name='lname',
                phone_number='0600000000',
                is_cashier=True
            )

    
    
    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            username='test_username',
            email='test@test.com',
            password='test_password',
            first_name='fname',
            last_name='lname',
            phone_number='0600000000',
        )

        self.assertEqual(user.username, 'test_username')
        self.assertEqual(user.email, 'test@test.com')
        self.assertEquals(user.check_password('test_password'), True)
        self.assertEqual(user.first_name, 'fname')
        self.assertEqual(user.last_name, 'lname')
        self.assertEqual(user.phone_number, '0600000000')
        
        self.assertTrue(user.is_cashier)
        
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        




        
        