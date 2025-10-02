from django.test import Client, TestCase
from django.utils import timezone

from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Тестовый заголовок",
            author="Автор Теста",
            content="Тестовое содержимое",
        )

    def test_post_creation(self):
        """Проверка, что пост создаётся корректно."""
        self.assertEqual(self.post.title, "Тестовый заголовок")
        self.assertEqual(self.post.author, "Автор Теста")
        self.assertEqual(self.post.content, "Тестовое содержимое")
        self.assertLessEqual(self.post.created_at, timezone.now())

    def test_post_str(self):
        """Проверка метода __str__."""
        self.assertEqual(str(self.post), "Тестовый заголовок")


class PostViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        Post.objects.create(title="Тест 1", author="Автор 1", content="Содержимое 1")
        Post.objects.create(title="Тест 2", author="Автор 2", content="Содержимое 2")

    def test_post_list_view_status(self):
        """Проверка, что страница /posts/ возвращает статус 200."""
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_content(self):
        """Проверка, что на странице отображаются заголовки постов."""
        response = self.client.get('/posts/')
        self.assertContains(response, 'Тест 1')
        self.assertContains(response, 'Тест 2')
