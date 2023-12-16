from django.shortcuts import render

# Create your views here.


def design_ltda_index(request): 
    return render(
        request, 
        "index.html"
    )
def design_ltda_elementos_designer(request): 
    return render(
        request, 
        "elementos_designer.html"
    )
def design_ltda_contatos(request): 
    return render(
        request, 
        "contatos.html"
    )