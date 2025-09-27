import logging, jsonpickle
from http import HTTPMethod
from fmconsult.utils.url import UrlUtil
from fipe.api import FipeApi

class Marcas(FipeApi):

    def __init__(self):
        super().__init__()

    def get_marcas(self, codigoTipoVeiculo):
        try:
            logging.info('listing FIPE Brands...')
            self.endpoint_url = UrlUtil().make_url(self.base_url, [codigoTipoVeiculo, 'brands'])
            res = self.call_request(
                http_method=HTTPMethod.GET,
                request_url=self.endpoint_url
            )
            return jsonpickle.decode(res)
        except:
            raise