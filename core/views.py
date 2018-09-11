from django.shortcuts import render
from django.conf import settings
import requests
from .forms import SubmitEmbed
from .serializer import AccountInvoiceSerializer

'''Used generatore insted of for loop'''

def save_by_generator(insert_data):
    for obj in insert_data:
        yield obj


'''Calling the api '''
# form = SubmitEmbed(request.POST)
            # if form.is_valid():
                # url = form.cleaned_data['url']
def save_embed(request):

    if request.method == "GET":
        try:
            r = requests.get('http://127.0.0.1:8000/INVOICE/ListView' )
            json = r.json()
            for obj in save_by_generator(json):
                    serializer = AccountInvoiceSerializer(data=obj)
                    if serializer.is_valid():
                        print(serializer)
                        embed = serializer.save()
                        # return render(request, 'embeds.html', {'embed': embed})

                # json = {'student_name':'satyam'}
                # for obj in json:
                #     serializer = AccountInvoiceSerializer(data=obj)
                #     if serializer.is_valid():
                #         print(serializer)
                #         embed = serializer.save()
                #         # return render(request, 'embeds.html', {'embed': embed})
        except Exception as e:
            print(e)

    else:
        pass
        # form = SubmitEmbed()

    return render(request, 'index.html', {})
