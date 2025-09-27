import logging, jsonpickle
from http import HTTPMethod
from fmconsult.utils.url import UrlUtil
from fipe.api import FipeApi

class AnosModelo(FipeApi):

    def __init__(self):
        super().__init__()

    def get_anos_by_modelo(self, codigoTipoVeiculo, codigoMarca, codigoModelo):
        try:
            logging.info(f'listing FIPE Years by Model {str(codigoModelo)}...')
            self.endpoint_url = UrlUtil().make_url(self.base_url, [codigoTipoVeiculo, 'brands', codigoMarca, 'models', codigoModelo, 'years'])
            res = self.call_request(
                http_method=HTTPMethod.GET,
                request_url=self.endpoint_url
            )
            return jsonpickle.decode(res)
        except:
            raise