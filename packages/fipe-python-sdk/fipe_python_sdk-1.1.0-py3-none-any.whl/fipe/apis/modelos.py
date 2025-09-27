import logging, jsonpickle
from http import HTTPMethod
from fmconsult.utils.url import UrlUtil
from fipe.api import FipeApi

class Modelos(FipeApi):

    def __init__(self):
        super().__init__()
        
    def get_modelos_by_marca(self, codigoTipoVeiculo, codigoMarca):
        try:
            logging.info(f'listing FIPE Models by Brand {str(codigoMarca)}...')
            self.endpoint_url = UrlUtil().make_url(self.base_url, [codigoTipoVeiculo, 'brands', codigoMarca, 'models'])
            res = self.call_request(
                http_method=HTTPMethod.GET,
                request_url=self.endpoint_url
            )
            return jsonpickle.decode(res)
        except:
            raise