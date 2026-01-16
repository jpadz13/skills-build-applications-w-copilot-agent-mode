from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, Leaderboard

User = get_user_model()

class BasicModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(str(user), 'testuser')

    def test_create_activity(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='pass')
        team = Team.objects.create(name='Test Team 2')
        activity = Activity.objects.create(user=user, type='run', duration=10, distance=1.5)
        self.assertEqual(str(activity), 'testuser2 - run')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', duration=20)
        self.assertEqual(str(workout), 'Test Workout')

    def test_create_leaderboard(self):
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='pass')
        leaderboard = Leaderboard.objects.create(user=user, score=50)
        self.assertEqual(str(leaderboard), 'testuser3 - 50')
