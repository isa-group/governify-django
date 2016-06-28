from django.http import HttpResponse

from models import Book



def governify(f):
    """ view decorator, the sole purpose to is 'rename' the function
    '_shortcircuitmiddleware' """
    def _governify(*args, **kwargs):
        return f(*args, **kwargs)
    return _governify

class ShortCircuitMiddleware(object):
    """ Middleware; looks for a view function named '_shortcircuitmiddleware'
    and short-circuits. Relies on the fact that if you return an HttpResponse
    from a view, it will short-circuit other middleware, see:
    https://docs.djangoproject.com/en/dev/topics/http/middleware/#process-request
     """
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.func_name == "_governify":
            return view_func(request, *view_args, **view_kwargs)
        else:
            return HttpResponse("No cumple.", content_type="text/plain",status=404)