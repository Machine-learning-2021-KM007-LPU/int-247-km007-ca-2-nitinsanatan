from django.shortcuts import render
import pickle
import sklearn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create your views here.

def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"HOME.html")    
def contact(request):
    return render(request,"Contact.html")    
def about(request):
    return render(request,"About.html")

def chart(request):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data'
    dataset = pd.read_csv(url)
    x = ['YES','NO']
    y = dataset.iloc[:, -1].value_counts().tolist()
    return render(request,"chart.html",{'x':x, 'data':y})


def result(request):
    knn='knn_model.sav'
    load_knn = pickle.load(open(knn, 'rb'))

    name=request.GET['Name']
    a2=  request.GET['A2']
    a3 = request.GET['A3']
    a4 = request.GET['A4']
    a5 = request.GET['A5']
    a6 = request.GET['A6']
    a7 = request.GET['A7']
    a8 = request.GET['A8']
    a11 = request.GET['A11']
    a14= request.GET['A14']
    

    lis = [[a2, a3, a4, a5, a6, a7, a8, 0.5, 0.5, a11, 1, 0, a14, 0.5]]

    print(lis)    

    ans= load_knn.predict(lis)    
    if ans==0:
        ans= "Your loan is expected to get approved."
    else:
        ans= "You are not meeting the criteria. Your Credit might not get accepted. "    

    return render(request,"Result.html",{'name':name,'ans':ans,'lis':lis})

        
