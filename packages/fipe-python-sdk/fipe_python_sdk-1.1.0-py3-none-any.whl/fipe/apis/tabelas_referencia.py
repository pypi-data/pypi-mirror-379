import logging, jsonpickle
from http import HTTPMethod
from fmconsult.utils.url import UrlUtil
from fipe.api import FipeApi

class TabelasReferencia(FipeApi):

    def __init__(self):
        super().__init__()
        self.endpoint_url = UrlUtil().make_url(self.base_url, ['references'])

    def get_tabelas_referencia(self):
        try:
            logging.info('listing FIPE reference tables...')
            res = self.call_request(
                http_method=HTTPMethod.GET,
                request_url=self.endpoint_url
            )
            return jsonpickle.decode(res)
        except:
            raise