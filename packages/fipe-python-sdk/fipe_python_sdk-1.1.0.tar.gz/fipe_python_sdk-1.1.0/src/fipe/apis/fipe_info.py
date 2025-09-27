import logging, jsonpickle
from http import HTTPMethod
from fmconsult.utils.url import UrlUtil
from fipe.api import FipeApi

class FipeInfo(FipeApi):

    def __init__(self):
        super().__init__()

    def get_fipe_info(self, codigoTipoVeiculo, codigoMarca, codigoModelo, codigoAnoModelo):
        try:
            logging.info(f'get Valor by parameters...')
            self.endpoint_url = UrlUtil().make_url(self.base_url, [codigoTipoVeiculo, 'brands', codigoMarca, 'models', codigoModelo, 'years', codigoAnoModelo])
            res = self.call_request(
                http_method=HTTPMethod.GET,
                request_url=self.endpoint_url
            )
            return jsonpickle.decode(res)
        except:
            raise