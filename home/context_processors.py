from . models import contact_page,hero

def credentials(request):
    try:
        contact=contact_page.objects.get(show=True)
    except:
        contact=None
    return{'credentials':contact,'hero':hero.objects.get(show=True)}