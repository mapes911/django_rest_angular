'''
should be separated into different files, but for this simple rest app demo, we'll leave it all here
'''
import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status
from .factories import *


class ExperienceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser1', 'test@test.com', 'foobar')
        self.user2 = User.objects.create_user('testuser2', 'test2@test.com', 'foobar')
        login = self.client.login(username='testuser1', password='foobar')
        self.assertTrue(login)
        self.experiences = []
        for _ in xrange(40):
            experience = ExperienceFactory.create(user=self.user)
            self.experiences.append(experience)

            for _ in xrange(5):
                ChapterFactory.create(experience=experience)

    def tearDown(self):
        del self.user
        del self.user2
        del self.experiences

    ''' Model Tests '''
    def test_model_my_chapters(self):
        ''' this is the only model test we really need here, just make sure the model method is accurate '''
        chapters = self.experiences[0].chapter_list()
        self.assertEqual(len(chapters), 5)

    ''' List View Tests '''
    def test_list_experiences(self):
        response = self.client.get(reverse('experience-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertEqual(json_response['count'], 40)
        self.assertEqual(len(json_response['results']), 30)

    ''' Detail View Tests - GET '''
    def test_experience_detail_get(self):
        response = self.client.get(reverse('experience-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertEqual(len(json_response['chapters']), 5)

    def test_experience_detail_get_logged_out(self):
        self.client.logout()
        self.test_experience_detail_get()

    def test_experience_detail_get_404(self):
        response = self.client.get(reverse('experience-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    ''' Detail View Tests - UPDATE/PUT '''
    def test_experience_detail_update(self):
        url = reverse('experience-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
            'moral': 'My New Moral'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_experience_detail_update_missing_field(self):
        url = reverse('experience-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_experience_detail_update_logged_out(self):
        self.client.logout()
        url = reverse('experience-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
            'moral': 'My New Moral'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_experience_detail_update_as_wrong_user(self):
        self.client.logout()
        self.client.login(username='testuser2', password='foobar')
        url = reverse('experience-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
            'moral': 'My New Moral'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ''' Detail View Tests - DELETE/DESTROY '''
    def test_experience_detail_destroy(self):
        url = reverse('experience-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Experience.DoesNotExist):
            Experience.objects.get(id=1)

    def test_experience_detail_destroy_404(self):
        url = reverse('experience-detail', kwargs={'pk': 999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_experience_detail_destroy_as_wrong_user(self):
        self.client.logout()
        self.client.login(username='testuser2', password='foobar')
        url = reverse('experience-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ChapterTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser1', 'test@test.com', 'foobar')
        self.user2 = User.objects.create_user('testuser2', 'test2@test.com', 'foobar')
        login = self.client.login(username='testuser1', password='foobar')
        self.assertTrue(login)

        self.experience = ExperienceFactory.create(user=self.user)
        self.chapter = ChapterFactory.create(experience=self.experience)

    def tearDown(self):
        del self.user
        del self.user2
        del self.experience
        del self.chapter

    ''' Detail View Tests - GET '''
    def test_chapter_detail_get(self):
        response = self.client.get(reverse('chapter-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertNotEqual(json_response['title'], '')

    def test_chapter_detail_get_logged_out(self):
        self.client.logout()
        self.test_chapter_detail_get()

    def test_chapter_detail_get_as_wrong_user(self):
        self.client.logout()
        self.client.login(username='testuser2', password='foobar')
        self.test_chapter_detail_get()

    def test_chapter_detail_get_404(self):
        response = self.client.get(reverse('chapter-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    ''' Detail View Tests - UPDATE/PUT '''
    def test_chapter_detail_update(self):
        url = reverse('chapter-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
            'body': 'My New Body'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chapter_detail_update_missing_field(self):
        url = reverse('chapter-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_chapter_detail_update_logged_out(self):
        self.client.logout()
        url = reverse('chapter-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
            'body': 'My New Body'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_chapter_detail_update_as_wrong_user(self):
        self.client.logout()
        self.client.login(username='testuser2', password='foobar')
        url = reverse('chapter-detail', kwargs={'pk': 1})
        data = {
            'title': 'My New Title',
            'body': 'My New Body'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    ''' Detail View Tests - DELETE/DESTROY '''
    def test_chapter_detail_destroy(self):
        url = reverse('chapter-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Chapter.DoesNotExist):
            Chapter.objects.get(id=1)

    def test_chapter_detail_destroy_404(self):
        url = reverse('chapter-detail', kwargs={'pk': 999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_chapter_detail_destroy_as_wrong_user(self):
        self.client.logout()
        self.client.login(username='testuser2', password='foobar')
        url = reverse('chapter-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
