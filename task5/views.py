from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


user_list = ['Andre', 'Alex', 'Mihail', 'Anna', 'Nadejda', 'Pit', 'Katrin']

# Create your views here.
def sign_up_by_html(request):
    global user_list
    info = {}
    context = {'info': info,}

    if request.method == 'POST':
            # Получаем данные:
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            # Обработка данных:
            if password == repeat_password and int(age) >= 18 and str(username) not in user_list:
                # Http ответ пользователю:
                return HttpResponse(f"Приветствуем, {username}!")
            else:
                if password != repeat_password:
                    info.update({'error': 'Пароли не совпадают'})
                elif int(age) < 18:
                    info.update({'error': 'Вы должны быть старше 18'})
                elif username in user_list:
                    info.update({'error': 'Пользователь уже существует'})
                return render(request, 'fifth_task/registration_page.html', context)

    # Если это GET
    return render(request, 'fifth_task/registration_page.html', context)



def sign_up_by_django(request):
    global user_list
    info = {}
    context = {'info': info, 'ContactForm': ContactForm()}

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Обработка данных:
            if password == repeat_password and int(age) >= 18 and str(username) not in user_list:
                # Http ответ пользователю:
                return HttpResponse(f"Приветствуем, {username}!")
            else:
                if password != repeat_password:
                    info.update({'error': 'Пароли не совпадают'})
                elif int(age) < 18:
                    info.update({'error': 'Вы должны быть старше 18'})
                elif username in user_list:
                    info.update({'error': 'Пользователь уже существует'})
                return render(request, 'fifth_task/registration_page.html', context)

    else:
        form = ContactForm()
    return render(request, 'fifth_task/registration_page.html', {'form': form})



