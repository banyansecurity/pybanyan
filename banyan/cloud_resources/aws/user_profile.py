import boto3
from banyan.bcolors import bcolors
from .base import ResourceBase


class UserProfile():
    def __init__(self, boto_session: boto3.Session):
        self._boto_session = boto_session
        self._user_profile = None

    @property
    def user_profile(self):
        if self._user_profile is None:
            self._user_profile = self._boto_session.client('sts').get_caller_identity()
        return self._user_profile
