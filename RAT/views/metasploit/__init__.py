from .android import *
@login_required

def methods(request):
    """
    View function for home page of site.
    """


    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'metasploit/android/methods.html',
        context={
        },
    )
