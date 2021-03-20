from django.shortcuts import render

# Create your views here.
def biss_view(request):
    return render(request,'testApp/biss.html')

def veg_view(request):
    return render(request,'testApp/veg.html')

def nonveg_view(request):
    return render(request,'testApp/nonveg.html')

def feedback_view(request):
    return render(request,'testApp/feedback.html')

def submit_view(request):
        return render(request,'testApp/submit.html')

def protein_view(request):
        return render(request,'testApp/protein.html')

def daibetes_view(request):
        return render(request,'testApp/daibetes.html')

def health_view(request):
        return render(request,'testApp/health.html')

def blood_view(request):
        return render(request,'testApp/blood.html')


def carbo_view(request):
        return render(request,'testApp/carbo.html')

def order_view(request):
        return render(request,'testApp/order.html')

def veglist_view(request):
        return render(request,'testApp/veglist.html')

def nonveglist_view(request):
        return render(request,'testApp/nonveglist.html')

def register_view(request):
        return render(request,'testApp/register.html')        
