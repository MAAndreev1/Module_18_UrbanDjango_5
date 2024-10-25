from django.shortcuts import render

# Create your views here.

def main_template(request):
    pagename = 'Главная страница'
    context = {'pagename': pagename,}
    return render(request, 'fourth_task/menu.html', context)

def shop_template(request):
    pagename = 'Игры'
    games = ['Cyberpunk 2077', 'State of Decay 2', 'Dragons Dogma']
    context = {
        'games': games,
        'pagename': pagename,
    }
    return render(request, 'fourth_task/shop_template.html', context)

def basket_template(request):
    pagename = 'Корзина'
    context = {'pagename': pagename,}
    return render(request, 'fourth_task/basket_template.html', context)