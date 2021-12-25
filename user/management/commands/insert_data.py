import json
import random
from datetime import datetime, timedelta

import pytz
from django.core.management.base import BaseCommand

from user.models import User, Activity
from backend.settings import BASE_DIR


class Command(BaseCommand):
    base_path = BASE_DIR
    setup_path = base_path + '/user/management/data/'
    timezones = pytz.all_timezones

    def generate_to_time(self, from_time):
        """

        :param from_time: activity from_time(datetime)
        :return: datetime - adds random hours from 1 to 10 to the from time
        """
        return from_time + timedelta(hours=random.randint(1, 10))

    def generate_from_time(self, min_year=2000, max_year=datetime.now().year):
        """
        :param min_year: setting default min_year as 2000, all the datetime created must be greater than 2000
        :param max_year: setting default min_year as current year, all the datetime created must be lesser than 2000
        :return: random datetime object from min_year to max_year
        """
        start = datetime(min_year, 1, 1, 00, 00, 00, tzinfo=pytz.UTC)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        return start + (end - start) * random.random()

    def random_timezone(self):
        """
        :return: random timezone
        """
        return self.timezones[random.randint(0, len(self.timezones) - 1)]

    def setup_data(self, count):
        """

        :param count: Number received from command line. default 100
        """
        json_file = open(self.setup_path + 'sample_data.json')
        users = json.load(json_file)
        for user in users[:count]:

            new_user = User(
                first_name=user['first_name'],
                last_name=user['last_name'],
                username=user['first_name'] + '_' + user['last_name'],
                email=user['email'],
                job_title=user['job_title'],
                ssn=user['ssn'],
                profile_picture=user['profile_pic'],
                phone_number=user['phone_number'],
                company=user['company'],
                tz=self.random_timezone(),
            )
            new_user.save()
            new_user.set_password(new_user.username[:5] + new_user.ssn[-4:])
            new_user.save()
            for _ in range(random.randint(1, 10)):
                from_time = self.generate_from_time()
                to_time = self.generate_to_time(from_time)
                activity = Activity(
                    user=new_user,
                    start_time=from_time,
                    end_time=to_time
                )
                activity.save()

    def add_arguments(self, parser):
        parser.add_argument('-l', '--length', nargs=1,
                            type=int, help='Number of data should be inserted')

    def handle(self, *args, **options):
        BUILD_DATA = {
            1: self.setup_data
        }
        for key, value in BUILD_DATA.items():
            print("Started '{} - {}' process".format(key,
                                                     BUILD_DATA[key].__name__))

            try:

                if options['length']:
                    count = options['length'][0] if 1 <= options['length'][0] <= 1000 else 100
                else:
                    count = 100
                print("Inserting {} data".format(count))
                BUILD_DATA[key](count)
                print("Completed '{} - {}' process".format(key, value.__name__))
            except Exception as e:
                print(
                    "Error Occurred in '{} - {}' process - {}".format(key, BUILD_DATA[key].__name__,
                                                                      e))
            print("\n")

    print('Completed Backend Setup')
