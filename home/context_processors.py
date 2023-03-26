from . models import contact_page

def credentials(request):
    return{'credentials':contact_page.objects.get(show=True)}