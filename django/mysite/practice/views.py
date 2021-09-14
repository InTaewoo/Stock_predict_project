from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post
import json
from django.db import connection
import pandas as pd
# Create your views here.

def index(request):
    financedata = []
    financedata_dic = {}
    # try:
    cursor = connection.cursor()
    query2 = 'SELECT * FROM `financedata` where st_cd = "000660";'
    print(query2)
    result=cursor.execute(query2)
    result=pd.DataFrame(cursor.fetchall())
    connection.commit()
    connection.close()
    # abc=pd.DataFrame(datas)
    print(abc)
    for i in range(len(result)):
        row = {
                'dates' : result.iloc[i,0][:10],
               'changes': result.iloc[i,6]
            # ,
            # 'dates': result.iloc[i, 0]
        }

        financedata.append(row)
    financedataJSON = json.dumps(financedata)
    return render(request,'index.html',{'financedataJSON':financedataJSON})
    print(result)
    # return render(request,'index.html')
def samsung(request):
    return render(request,'samsung.html')

def sk_hynicx(request):
    return render(request,'sk_hynicx.html')

def hyundai(request):
    return render(request,'hyundai.html')

def lg_chem(request):
    return render(request,'lg_chem.html')

def charts(request):
    return render(request,'charts.html')

print(query2)

