from applications.home.models import Home

# Procesor para recuperar el telefono y el email para el footer

def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.contact_phone,
        'email': home.contact_email,
    }