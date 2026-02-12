from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Очистка данных
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Marvel и DC команды
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Супергерои
        users = [
            User.objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel),
            User.objects.create_user(email='captain@marvel.com', username='captain', team=marvel),
            User.objects.create_user(email='batman@dc.com', username='batman', team=dc),
            User.objects.create_user(email='superman@dc.com', username='superman', team=dc),
        ]

        # Активности
        Activity.objects.create(user=users[0], type='run', duration=30)
        Activity.objects.create(user=users[1], type='cycle', duration=45)
        Activity.objects.create(user=users[2], type='swim', duration=25)
        Activity.objects.create(user=users[3], type='walk', duration=60)

        # Лидерборд
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=80)
        Leaderboard.objects.create(user=users[3], points=70)

        # Тренировки
        Workout.objects.create(user=users[0], description='Chest day')
        Workout.objects.create(user=users[1], description='Leg day')
        Workout.objects.create(user=users[2], description='Back day')
        Workout.objects.create(user=users[3], description='Cardio')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
