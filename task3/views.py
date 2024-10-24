from django.shortcuts import render

# Create your views here.

def main_template(request):
    title = 'Главная страница'
    button_main_text = 'Главная'
    button_shop_text = 'Магазин'
    button_basket_text = 'Корзина'
    context = {
        'title': title,
        'button_main_text': button_main_text,
        'button_shop_text': button_shop_text,
        'button_basket_text': button_basket_text,
    }
    return render(request, 'third_task/main_template.html', context)

def shop_template(request):
    return render(request, 'third_task/shop_template.html')

def basket_template(request):
    return render(request, 'third_task/basket_template.html')