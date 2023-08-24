from rest_framework.throttling import UserRateThrottle


class OnlyFiveThrottle(UserRateThrottle):
    scope = 'onlyfive'
