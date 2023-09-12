from django.shortcuts import render

# Create your views here.
def main(request):
    context = {
        'name': 'Mika Ahmad Al Husseini',
        'npm': 2206826476,
        'kelas': 'PBP-A',
    }
    return render(request, "main.html", context)

def lightcones(request):
    context = {
        'name': 'Cruising in the Stellar Sea',
        'amount': 5,
        'description': """Coursing 'tween the sea of stars,
                        they cruise with the speed of a rainbow's chromatic flash.
                        A journey of hunting undying abominations,
                        collecting cures and miracles,
                        and seeking deliverance.
                        Akin to a vow unbroken, their voyage will be,
                        ad infinitum.""",
        'rarity': 5,
        'lc_path': 'The Hunt',
        'base_atk': 635,
        'base_hp': 1058,
        'base_def': 396,
    }

    return render(request, "lightcones.html", context)