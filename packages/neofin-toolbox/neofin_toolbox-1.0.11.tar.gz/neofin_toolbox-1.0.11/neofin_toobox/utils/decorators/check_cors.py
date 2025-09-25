from functools import wraps
from neofin_toobox.utils.helpers import handle_cors_options


def route_with_check_cors(bp, path, allowed_origins, **kwargs):
    def decorator(func):
        @wraps(func)
        def wrapped_func(*args, **kw):
            # Pega o origin do request
            origin = bp.current_request.headers.get('origin', '') or bp.current_request.headers.get('referer')

            response = func(*args, **kw)

            headers = {
                "Access-Control-Allow-Origin": origin,
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Empcookie",
                "Access-Control-Allow-Credentials": "true",
            }

            if hasattr(response, "headers"):
                response.headers.update(headers)
                return response

            if isinstance(response, tuple):
                data, status = response
                return data, status, headers

            return response, 200, headers

        bp.route(path, **kwargs)(wrapped_func)

        def options_handler(*args, **kw):
            return handle_cors_options(bp, allowed_origins)

        bp.route(path, methods=['OPTIONS'])(options_handler)

        return wrapped_func

    return decorator
