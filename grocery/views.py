from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from grocery.models import Grocery

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'grocery/signup.html'

class GroceryListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        # Get the data GET parameter
        date = self.request.GET.get("date")
        if date:
            # Return a filtered queryset
            return Grocery.objects.filter(user = self.request.user).filter(created_at__icontains=date)
        return Grocery.objects.filter(user = self.request.user)

    
def add_grocery(request):
    if request.method == 'POST':
        name = request.POST.get('itemname',False)
        quantity = request.POST.get('quentity',False)
        status = request.POST.get('status',False)
        created_at = request.POST.get('created_at',False)
        newGrocery = Grocery(name=name,quantity=quantity,status=status,user= request.user,created_at=created_at)
        newGrocery.save()
        return redirect('/')
    return render(request ,'grocery/add_item.html')


def update_grocery(request,id):
    grocery_item = get_object_or_404(Grocery,pk=id)

    if request.method == 'POST':
        name = request.POST.get('itemname',False)
        quantity = request.POST.get('quentity',False)
        status = request.POST.get('status',False)
        created_at = request.POST.get('created_at',False)
        Grocery.objects.filter(id=id).update(name=name,quantity=quantity,status=status,user= request.user,created_at=created_at)
        return redirect('/')

    return render(request ,'grocery/update_item.html',{'item':grocery_item})


def delete_grocery(request,id):
    Grocery.objects.get(id=id).delete()
    return redirect("/")  

