from django.shortcuts import render
from joblib import load

model=load('./../Mobile price/model.joblib')
# Create your views here.
def predictor(request):
    return render(request,'main.html')

def formInfo(request):
    battery_power=request.GET['battery_power']
    blue=request.GET['blue']
    clock_speed=request.GET['clock_speed']
    dual_sim=request.GET['dual_sim']
    fc=request.GET['fc']
    four_g=request.GET['four_g']
    int_memory=request.GET['int_memory']
    m_dep=request.GET['m_dep']
    mobile_wt=request.GET['mobile_wt']
    n_cores=request.GET['n_cores']
    pc=request.GET['pc']
    px_height=request.GET['px_height']
    px_width=request.GET['px_width']
    ram=request.GET['ram']
    sc_h=request.GET['sc_h']
    sc_w=request.GET['sc_w']
    talk_time=request.GET['talk_time']
    three_g=request.GET['three_g']
    touch_screen=request.GET['touch_screen']
    wifi=request.GET['wifi']

    y_pred=model.predict([[battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,
                   sc_h,sc_w,talk_time,three_g, touch_screen,wifi]])
    if y_pred[0]<=0:
        y_pred='Price is very low'
    elif y_pred[0]<=1:
        y_pred='Price is lower'
    elif y_pred[0]<=2:
        y_pred='Price is high'
    elif y_pred[0] <=3:
        y_pred='Price is very high'

    return render (request,'result.html',{'result': y_pred})