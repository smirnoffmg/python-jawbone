# -*- coding: utf-8 -*-
try:
    from urllib.parse import urljoin
except Exception:
    from urlparse import urljoin

import requests

from .exceptions import JawboneException


class JawboneClient(object):
    BASE_URL = 'https://jawbone.com/'
    TOKEN = None

    def __init__(self, token):
        self.TOKEN = token

    def __get_headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.TOKEN),
            'Accept': 'application/json'
        }

    def __get(self, url, **params):
        full_url = urljoin(self.BASE_URL, url)
        headers = self.__get_headers()

        r = requests.get(full_url, headers=headers, params=params)
        if r.status_code == 200:
            return r.json()
        raise JawboneException(r.content)

    # Body events (https://jawbone.com/up/developer/endpoints/body)

    def get_body_events(self, date=None, page_token=None, start_time=None,
                        end_time=None, updated_after=None, limit=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/body_events',
            date=date,
            page_token=page_token,
            start_time=start_time,
            end_time=end_time,
            updated_after=updated_after,
            limit=limit
        )

    def get_body_event(self, xid):
        return self.__get('/nudge/api/v.1.1/users/@me/body_events/{}'.format(xid))

    # Band events (https://jawbone.com/up/developer/endpoints/bandevents)

    def get_band_events(self, date=None, start_time=None, end_time=None, created_after=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/bandevents',
            date=date,
            start_time=start_time,
            end_time=end_time,
            created_after=created_after
        )

    # Heart rates (https://jawbone.com/up/developer/endpoints/heartrate)

    def get_heart_rates(self, date=None, page_token=None, start_time=None,
                        end_time=None, updated_after=None, limit=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/heartrates',
            date=date,
            page_token=page_token,
            start_time=start_time,
            end_time=end_time,
            updated_after=updated_after,
            limit=limit
        )

    # Custom events (https://jawbone.com/up/developer/endpoints/custom)

    def get_custom_events(self, date=None, page_token=None, start_time=None,
                          end_time=None, updated_after=None, limit=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/generic_events',
            date=date,
            page_token=page_token,
            start_time=start_time,
            end_time=end_time,
            updated_after=updated_after,
            limit=limit
        )

    # Goals (https://jawbone.com/up/developer/endpoints/goals)

    def get_goals(self):
        return self.__get('/nudge/api/v.1.1/users/@me/goals')

    # Meals (https://jawbone.com/up/developer/endpoints/meals)

    def get_meals(self, date=None, page_token=None, start_time=None,
                  end_time=None, updated_after=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/meals',
            date=date,
            page_token=page_token,
            start_time=start_time,
            end_time=end_time,
            updated_after=updated_after,
        )

    # Mood (https://jawbone.com/up/developer/endpoints/mood)

    def get_mood(self, date=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/mood',
            date=date
        )

    # Moves (/nudge/api/v.1.1/users/@me/moves)

    def get_moves(self, date=None, page_token=None, start_time=None,
                  end_time=None, updated_after=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/moves',
            date=date,
            page_token=page_token,
            start_time=start_time,
            end_time=end_time,
            updated_after=updated_after,
        )

    # Sleeps (https://jawbone.com/up/developer/endpoints/sleeps)

    def get_sleeps(self, date=None, page_token=None, start_time=None,
                   end_time=None, updated_after=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/sleeps',
            date=date,
            page_token=page_token,
            start_time=start_time,
            end_time=end_time,
            updated_after=updated_after,
        )

    # Timezone (https://jawbone.com/up/developer/endpoints/timezone)

    def get_timezone(self, date=None, start_time=None, end_time=None,
                     timestamp=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/timezone',
            date=date,
            start_time=start_time,
            end_time=end_time,
            timestamp=timestamp,
        )

    # Trends (https://jawbone.com/up/developer/endpoints/trends)

    def get_trends(self, end_date=None, bucket_size=None, num_buckets=100):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/trends',
            end_date=end_date,
            bucket_size=bucket_size,
            num_buckets=num_buckets
        )

    # User (https://jawbone.com/up/developer/endpoints/user)

    def get_user(self):
        return self.__get('/nudge/api/v.1.1/users/@me')

    def get_friends(self):
        return self.__get('/nudge/api/v.1.1/users/@me/friends')

    # Workouts (https://jawbone.com/up/developer/endpoints/workouts)

    def get_workouts(self, date=None, page_token=None, start_time=None,
                     end_time=None, updated_after=None):
        return self.__get(
            '/nudge/api/v.1.1/users/@me/workouts',
            date=date,
            page_token=page_token,
            start_time=start_time,
            end_time=end_time,
            updated_after=updated_after,
        )
