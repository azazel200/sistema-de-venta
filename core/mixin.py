from django.shortcuts import redirect
from django.urls import reverse_lazy

class StaffRequiredMixin(object):
    """
    Este mixin requerirar que el usuario tiene que estar logueado 
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)