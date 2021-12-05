from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
        'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def handler_view(request, recipe):
    num = 1
    if request.GET.get('servings') is not None:
        num = int(request.GET.get('servings'))
    rec = {key: num * value for key, value in DATA[recipe].items()}
    context = {
        'recipe': rec
    }
    return render(request, 'calculator/index.html', context)