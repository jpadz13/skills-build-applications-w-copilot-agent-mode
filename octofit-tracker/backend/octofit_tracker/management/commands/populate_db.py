
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password'),
        ]

        # Assign teams (assuming a profile or custom user model is needed for team relation)
        # If not, this can be omitted or handled differently

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, distance=5)
        Activity.objects.create(user=users[1], type='cycle', duration=60, distance=20)
        Activity.objects.create(user=users[2], type='swim', duration=45, distance=2)
        Activity.objects.create(user=users[3], type='walk', duration=90, distance=8)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning run', duration=30)
        Workout.objects.create(name='Strength Training', description='Upper body workout', duration=45)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=80)
        Leaderboard.objects.create(user=users[2], score=120)
        Leaderboard.objects.create(user=users[3], score=110)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
