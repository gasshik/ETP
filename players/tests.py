from django.test import Client, TestCase
from django.urls import reverse

from players.models import Player


class PlayerModelTest(TestCase):
    def setUp(self):
        self.player = Player.objects.create(
            nickname="s1mple", first_name="Oleksandr", last_name="Kostyliev", country="Ukraine"
        )

    def test_player_content(self):
        self.assertEqual(self.player.nickname, "s1mple")
        self.assertEqual(str(self.player), "s1mple")


class PlayerViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Player.objects.create(nickname="ZywOo", country="France")

    def test_player_list_view(self):
        url = reverse("player_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ajax_filter(self):
        url = reverse("player_list")

        response = self.client.get(
            url, {"country": "France"}, **{"HTTP_X_REQUESTED_WITH": "XMLHttpRequest"}
        )

        print(f"\n[DEBUG] Тест стучится по адресу: {url}")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertIn("html", response.json())


