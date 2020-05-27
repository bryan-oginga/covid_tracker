from django.shortcuts import render
import requests
import json
from chartit import DataPool, Chart,PivotDataPool, PivotChart


def HomePageView(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {
        "country" : "kenya"
    }

    

    headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e774d241f9msh2ae2efebe13b562p193669jsn03c0aa8c6b1c"
    }
    
    response = requests.request("GET", url, headers=headers,params=querystring).json()

   
    data = response['response']
    cases = data[0]

    print(cases)

    context = {

      "all" : cases['cases']['total'],
      "recovered" : cases['cases']['recovered'],
      "new" : cases['cases']['new'],
      "critical" : cases['cases']['critical'],
      "deaths" : cases['deaths']['total'],

    }
    
    return render(request,'index.html',context)


