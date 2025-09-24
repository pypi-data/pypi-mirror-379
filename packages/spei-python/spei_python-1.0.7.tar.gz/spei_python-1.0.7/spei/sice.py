import logging
from typing import Any, Dict, Optional, Tuple, Type
from urllib.parse import urljoin

import requests

from spei.requests import CDARequest
from spei.resources import CDA
from spei.resources.acuse import Acuse

logger = logging.getLogger('sice')
logger.setLevel(logging.DEBUG)


class BaseClient(object):
    def __init__(
        self,
        host: str,
        verify: bool = False,
        http_client: Type[requests.Session] = requests.Session,
        auth: Optional[Tuple[str, str]] = None,
    ) -> None:
        self.host = host
        self.session = http_client()
        self.session.headers.update(
            {
                'Content-Type': 'application/xml; charset=cp850',
                'User-Agent': 'Fondeadora/SICE/v0.52.0',
            },
        )
        self.session.verify = verify
        if auth:
            self.session.auth = auth

    def registra_cda(
        self,
        cda_data: Dict[str, Any],
        endpoint: str = '/enlace-cep/EnvioCdaPortTypeImpl?wsdl',
    ) -> Acuse:
        orden = CDA(**cda_data)
        soap_request = CDARequest(orden).to_string()
        logger.info(soap_request)

        response = self._make_request(soap_request, endpoint)

        try:
            return Acuse.from_xml(response.text)
        except Exception:
            logger.exception(f'Error parsing Acuse response: {response.text}')
            raise

    def _make_request(self, soap_request: bytes, endpoint: str) -> requests.Response:
        url = urljoin(self.host, endpoint)
        response = self.session.post(data=soap_request, url=url)
        logger.info(response.text)
        response.raise_for_status()

        return response
