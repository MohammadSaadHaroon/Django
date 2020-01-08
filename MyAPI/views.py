from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import ApprovalForm
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from . models import approvals
from . serializers import approvalsSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class = approvalsSerializers

def ohevalue(df):
    ohe_col =joblib.load("/Users/PC/PycharmProjects/api/MyAPI/model_joblib.pkl")
    df_processed = pd.get_dummies(df)
    newdict = {}
    for i in ohe_col:
        if i in df_processed:
            newdict[i]=df_processed[i].values
        else:
            newdict[i]=0
        newdf =pd.DataFrame(newdict)
        return newdf


# def myform(request):
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             myform = form.save(commit = False)
#             #myfrom.save()
#     else:
#         form = MyForm()
#     #return render(request, 'myform/form.html',{'form': form})

#@api_view(["POST"])
def approvereject(request):
    try:
        mdl =joblib.load("/Users/PC/PycharmProjects/api/MyAPI/model_joblib.pkl")
        mydata = pd.read_csv("/Users/PC/Documents/python/s.csv")
        mydata =request.data
        unit =np.array(list(mydata.values()))
        unit =unit.reshape(1, -1)
        scalers = joblib.load("/Users/PC/PycharmProjects/api/MyAPI/model_joblib.pkl")
        X = scalers.transform(unit)
        y_pred=mdl.predict([[]])
        newdf = pd.DataFrame(y_pred, columns=['Status'])
        newdf = newdf.replace({True: 'Approved', False:'Rejected'})
        return JsonResponse('Your Status is {}'.format(newdf), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def cxcontact(request):

    if request.method=='POST':
        form =ApprovalForm(request.POST)
        if form.is_valid():
            Question = form.cleaned_data['Question']
            Clearmarks = form.cleaned_data['Clearmarks']
            Obtainmarks = form.cleaned_data['Obtainmarks']
            Time = form.cleaned_data['Time']

            myDict= (request.POST).dict()
            df = pd.DataFrame(myDict, index=[0])
            answer= approvereject(ohevalue(df))
            messages.success(request, 'Application Status: {}'.format(answer))
    form = ApprovalForm()

    return render(request, 'myform/cxform.html', {'form':form})