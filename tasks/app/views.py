from django.shortcuts import render,redirect
import time
# Create your views here.
def index(request):
    if 'elapsed_time' not in request.session:
        request.session['elapsed_time']=0

    if 'start_time' not in request.session:
        request.session['start_time']=None
        request.session['elapsed_time']=0
        request.session['running']=False

    elapsed=request.session.get('elapsed_time',0)
    if request.session['running']:
        elapsed=time.time()-request.session['start_time'] 
    hours,rem=divmod(int(elapsed),3600)
    minutes,seconds=divmod(rem,60)       
    return render(request,'index.html',{
        'hours':f"{hours:02d}",
        'minutes':f"{minutes:02d}",
        'seconds':f"{seconds:02d}"
    })




def start(request):
    if request.method == "POST" and not request.session.get('running', False):
        request.session['start_time'] = time.time() - request.session.get('elapsed_time', 0)
        request.session['running'] = True
    return redirect('index') 


def pause(request):
    if request.method == 'POST' and request.session.get('running', False):
        request.session['elapsed_time'] = time.time() - request.session['start_time']
        request.session['running'] = False
    return redirect('index') 

def reset(request):
    if request.method == 'POST':
        request.session['start_time'] = None
        request.session['elapsed_time'] = 0
        request.session['running'] = False
    return redirect('index')  


        
