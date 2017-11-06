from django.shortcuts import render, get_object_or_404

# Create your views here.

###################################################################################
################################### FRONT #########################################
###################################################################################
def get_list(request):

    return render(request, 'wishlist/front/items/list.html')