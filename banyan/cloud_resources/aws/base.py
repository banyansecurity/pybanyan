"""base class for cloud resource management"""
from abc import ABC, abstractmethod, abstractproperty
import boto3
from banyan.api import BanyanApiClient


class ResourceBase(ABC):
    """
    base class for cloud resource type
    Args:
        ABC([type]): [description]
    """

    def __init__(self, boto_session: boto3.Session, config: dict, api_client: BanyanApiClient, user_profile):
        if not boto_session:
            raise AttributeError('boto_session is missing')
        self._boto_session = boto_session
        self.config = config
        self._client = api_client
        self._user_profile = user_profile
        super().__init__()

    def list(self, include_tags=False, tag_name=None, tag_value=None):
        """
        List Cloud Resource
        Args:
            include_tags(bool, optional): [include Tags in response]. Defaults to False.
            tag_name([type], optional): [filter by tag name]. Defaults to None.
            tag_value([type], optional): [filter by tag value]. Defaults to None.

        Returns:
            [type]: [list of cloud resource]
        """
        result = self.client.inventory.list(
            include_tags, tag_name, tag_value, self.resource_type)
        return result

    def addAccountTags(self) -> list:
        tags = []
        tags.append(
            {'name': self.bnn_account_tag, 'value': self.account})
        tags.append(
            {'name': self.bnn_user_name_tag, 'value': self.user_name})
        return tags

    @abstractmethod
    def sync(self, region=None):
        """sync cloud resource with banyan cloud inventory"""

    @abstractproperty
    def resource_type(self) -> str:
        """cloud resource type i.e. ec2, lb, rds"""

    @property
    def boto_session(self) -> boto3.Session:
        """
        Gets/sets the boto3 session token profile
        """
        return self._boto_session

    @boto_session.setter
    def boto_session(self, value: boto3.Session) -> None:
        self._boto_session = value

    @property
    def client(self) -> BanyanApiClient:
        """
        Gets/sets the banyan API Client
        """
        return self._client

    @client.setter
    def client(self, value: BanyanApiClient) -> None:
        self._client = value

    @property
    def user_profile(self):
        return self._user_profile.user_profile

    @property
    def user_name(self) -> str:
        return self._user_profile['UserId'].split(':')[-1]

    @property
    def account(self) -> str:
        return self._user_profile['Account']

    @property
    def bnn_user_name_tag(self) -> str:
        return "bnn.cloudresource.sync.user_name"

    @property
    def bnn_account_tag(self) -> str:
        return "bnn.cloudresource.sync.account"
