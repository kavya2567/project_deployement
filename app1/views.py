from django.shortcuts import render, redirect
from app1.forms import employee_delete, employee_form
from app1.models import employee
from django.http import HttpResponse

def new_employee(request):
    data = employee.objects.all()
    form = employee_form()

    if request.method == 'POST':
        form = employee_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'data': data,
        'form': form
    }
    return render(request, 'home.html', context)
def update(request, id):
    emp = employee.objects.get(id=id)
    form = employee_form(instance=emp)

    if request.method == 'POST':
        form = employee_form(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('home_page')

    context = {
        'form': form
    }
    return render(request, 'update_emp.html', context)


def delete(request, id):
    def_username = 'kavya'
    def_password = 'kavya@123'
    std = employee.objects.get(id=id)
    del_form = employee_delete()
    if request.method == 'POST':
        del_form = employee_delete(request.POST)
        if del_form.is_valid():
            user = del_form.cleaned_data['username']
            password = del_form.cleaned_data['password']

            if user == def_username and password == def_password:
                std.delete()
                return redirect('home_page')
            else:
                return HttpResponse('Invalid username and password')
    return render(request, 'delete_emp.html', {'del_form': del_form})