from .android import *
from django.contrib.auth.decorators import login_required

@login_required
def methods(request):
    """
    View function for home page of site.
    """


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'pupy/android/methods.html',
        context={
        },
    )
