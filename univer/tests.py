from rest_framework.test import APITestCase
from model_mommy import mommy

from univer.models import Student


class StudentApiTests1(APITestCase):
    def test_get_students(self):
        res = self.client.get('/students/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 0)

    def test_post_students(self):
        new_stud = {
            'last_name': 'Иванов',
            'first_name': 'Иван',
            'second_name': 'Иванович',
            'id_number': '123456',
        }
        res = self.client.post('/students/', new_stud)
        self.assertEqual(res.status_code, 201)
        self.assertGreater(res.data['id'], 0)
        temp = res.data
        temp.pop('id')
        temp.pop('grade_set')
        self.assertEqual(temp, new_stud)
        
        res = self.client.get('/students/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 1)


class StudentApiTests2(APITestCase):
    def setUp(self):
        self.student = mommy.make(Student)
        return super().setUp()

    def test_get_students(self):
        res = self.client.get('/students/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data['count'], 1)
        temp = res.data['results'][0]
        self.assertEqual(temp['last_name'], self.student.last_name)
        self.assertEqual(temp['first_name'], self.student.first_name)
        self.assertEqual(temp['second_name'], self.student.second_name)
        self.assertEqual(temp['id_number'], self.student.id_number)
