from flask import jsonify

ERROR_HANDLER_MAPPING = {
  400: "handle_bad_request",
  401: "handle_unauthorized",
  403: "handle_forbidden",
  404: "handle_not_found",
  405: "handle_method_not_allowed",
  408: "handle_request_timeout",
  409: "handle_conflict",
  410: "handle_gone",
  429: "handle_too_many_requests",
  500: "handle_internal_server_error",
  501: "handle_not_implemented",
  502: "handle_bad_gateway",
  503: "handle_service_unavailable",
  504: "handle_gateway_timeout"
}

class HTTP_Error():
    """ Base class for HTTP Errors """

    def __init__(self, id="", name="", hint="", message="", code=500) -> None:
        self.id = id
        self.name = name
        self.hint = hint
        self.message = message
        self.code = code
        super().__init__(self.id, self.name, self.hint, self.message)

    def to_dict(self):
        dict = {'code':self.code , 'name':self.name, 'hint':self.hint, 'message':self.message, 'id':self.id}
        return dict


## Client error classes
class Bad_Request_Error(HTTP_Error):
    def __init__(self, id="bad_request", name="Bad Request", hint="Check request syntax and parameters.", message="The server could not understand the request due to invalid syntax.", code=400):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Unauthorized_Error(HTTP_Error):
    def __init__(self, id="unauthorized", name="Unauthorized", hint="Ensure valid authentication credentials are provided.", message="Authentication is required and has failed or not been provided.", code=401):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Forbidden_Error(HTTP_Error):
    def __init__(self, id="forbidden", name="Forbidden", hint="Check user permissions and access control.", message="You do not have permission to access this resource.", code=403):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Not_Found_Error(HTTP_Error):
    def __init__(self, id="not_found", name="Not Found", hint="Verify the endpoint or resource identifier.", message="The requested resource could not be found.", code=404):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Method_Not_Allowed_Error(HTTP_Error):
    def __init__(self, id="method_not_allowed", name="Method Not Allowed", hint="Check allowed HTTP methods for this endpoint.", message="The HTTP method used is not supported for this resource.", code=405):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Request_Timeout_Error(HTTP_Error):
    def __init__(self, id="request_timeout", name="Request Timeout", hint="Optimize client request timing or retry strategy.", message="The server timed out waiting for the request.", code=408):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Conflict_Error(HTTP_Error):
    def __init__(self, id="conflict", name="Conflict", hint="Resolve resource state conflicts before retrying.", message="The request could not be completed due to a conflict with the current state of the resource.", code=409):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Gone_Error(HTTP_Error):
    def __init__(self, id="gone", name="Gone", hint="Resource has been permanently removed; update client logic.", message="The requested resource is no longer available and will not be restored.", code=410):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Too_Many_Requests_Error(HTTP_Error):
    def __init__(self, id="too_many_requests", name="Too Many Requests", hint="Implement exponential backoff or rate limiting.", message="You have sent too many requests in a given amount of time.", code=429):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

## Server Error Classes
class Internal_Server_Error(HTTP_Error):
    def __init__(self, id="internal_server_error", name="Internal Server Error", hint="Check server logs and exception trace.", message="The server encountered an unexpected condition.", code=500):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Not_Implemented_Error(HTTP_Error):
    def __init__(self, id="not_implemented", name="Not Implemented", hint="Verify endpoint support and implementation status.", message="The server does not support the functionality required to fulfill the request.", code=501):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Bad_Gateway_Error(HTTP_Error):
    def __init__(self, id="bad_gateway", name="Bad Gateway", hint="Check upstream service availability and response.", message="The server received an invalid response from the upstream server.", code=502):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Service_Unavailable_Error(HTTP_Error):
    def __init__(self, id="service_unavailable", name="Service Unavailable", hint="Retry later or monitor server health.", message="The server is currently unable to handle the request due to overload or maintenance.", code=503):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

class Gateway_Timeout_Error(HTTP_Error):
    def __init__(self, id="gateway_timeout", name="Gateway Timeout", hint="Check upstream server responsiveness.", message="The server did not receive a timely response from the upstream server.", code=504):
        super().__init__(id=id, name=name, hint=hint, message=message, code=code)

ERROR_CLASS_MAPPING = {
  400: Bad_Request_Error,
  401: Unauthorized_Error,
  403: Forbidden_Error,
  404: Not_Found_Error,
  405: Method_Not_Allowed_Error,
  408: Request_Timeout_Error,
  409: Conflict_Error,
  410: Gone_Error,
  429: Too_Many_Requests_Error,
  500: Internal_Server_Error,
  501: Not_Implemented_Error,
  502: Bad_Gateway_Error,
  503: Service_Unavailable_Error,
  504: Gateway_Timeout_Error
}

def general_error_handler(exception, request, response):
    return jsonify(ERROR_HANDLER_MAPPING[exception.error.code](exception.error.code, request, response))

def handle_bad_request(code, request, response):
    """400 Bad Request"""
    # Handle malformed or invalid client request
    return ERROR_CLASS_MAPPING[code]()

def handle_unauthorized(code, request, response):
    """401 Unauthorized"""
    # Handle missing or invalid authentication
    return ERROR_CLASS_MAPPING[code]()

def handle_forbidden(code, request, response):
    """403 Forbidden"""
    # Handle access denial despite authentication
    return ERROR_CLASS_MAPPING[code]()

def handle_not_found(code, request, response):
    """404 Not Found"""
    # Handle missing resource
    return ERROR_CLASS_MAPPING[code]()

def handle_method_not_allowed(code, request, response):
    """405 Method Not Allowed"""
    # Handle unsupported HTTP method
    return ERROR_CLASS_MAPPING[code]()

def handle_request_timeout(code, request, response):
    """408 Request Timeout"""
    # Handle client-side delay
    return ERROR_CLASS_MAPPING[code]()

def handle_conflict(code, request, response):
    """409 Conflict"""
    # Handle resource state conflict
    return ERROR_CLASS_MAPPING[code]()

def handle_gone(code, request, response):
    """410 Gone"""
    # Handle permanently removed resource
    return ERROR_CLASS_MAPPING[code]()

def handle_too_many_requests(code, request, response):
    """429 Too Many Requests"""
    # Handle rate limiting
    return ERROR_CLASS_MAPPING[code]()

def handle_internal_server_error(code, request, response):
    """500 Internal Server Error"""
    # Handle generic server failure
    return ERROR_CLASS_MAPPING[code]()

def handle_not_implemented(code, request, response):
    """501 Not Implemented"""
    # Handle unsupported server functionality
    return ERROR_CLASS_MAPPING[code]()

def handle_bad_gateway(code, request, response):
    """502 Bad Gateway"""
    # Handle invalid upstream response
    return ERROR_CLASS_MAPPING[code]()

def handle_service_unavailable(code, request, response):
    """503 Service Unavailable"""
    # Handle server overload or downtime
    return ERROR_CLASS_MAPPING[code]()

def handle_gateway_timeout(code, request, response):
    """504 Gateway Timeout"""
    # Handle upstream timeout
    return ERROR_CLASS_MAPPING[code]()
