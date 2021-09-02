from django.shortcuts import render

# Create your views here.
def bags_list(request):
    return render(request,'bags/bags_list.html')