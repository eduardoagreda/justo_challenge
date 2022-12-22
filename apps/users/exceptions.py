from apps.hits.status import NOT_FOUND

from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.exceptions import APIException

class NotFoundException(APIException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = {'status': HTTP_404_NOT_FOUND, 'data': None, 'message':NOT_FOUND}
    default_code = 'not_found'