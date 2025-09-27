import os
from fmconsult.http.api import ApiBase

class FipeApi(ApiBase):
    
    def __init__(self):
        try:
            self.subscription_token = os.environ['fipe.api.token']
            
            self.base_url = 'https://fipe.parallelum.com.br/api/v2'
            self.headers = {
                'X-Subscription-Token': self.subscription_token
            }
        except:
            raise