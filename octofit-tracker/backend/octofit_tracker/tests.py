from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='marvel', members=['Test User'])
        self.assertEqual(team.name, 'marvel')
        self.assertIn('Test User', team.members)

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', activity='Running', duration=30)
        self.assertEqual(activity.user, 'Test User')
        self.assertEqual(activity.activity, 'Running')
        self.assertEqual(activity.duration, 30)

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='marvel', points=100)
        self.assertEqual(lb.team, 'marvel')
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', suggested_for='marvel')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.suggested_for, 'marvel')
