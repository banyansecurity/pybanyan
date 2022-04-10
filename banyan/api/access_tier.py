from banyan.api.base import ApiBase
from banyan.model.access_tier import AccessTier, AccessTierInfo

class AccessTierAPI(ApiBase):
    class Meta:
        data_class = AccessTier
        info_class = AccessTierInfo
        supports_paging = True
        list_uri = '/v2/access_tier'
        insert_uri = '/v2/access_tier'
        delete_uri = '/v2/access_tier/ID'
        obj_name = 'access_tier'
