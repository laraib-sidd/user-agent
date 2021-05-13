from django.shortcuts import render
from .models import UserAgentTrack
import datetime
# Create your views here.

def index(request):
    D = {}
    now = datetime.datetime.now()
    time = now.strftime("%B %d %Y, %H:%M:%S")
    D["time"] = time
    user_agent = request.headers['User-Agent']
    try:
        print('try reached')
        user = UserAgentTrack.objects.get(user_agent = user_agent)
        user.count = user.count + 1
        user.save()
        count = user.count + 1
    except:
        print('except reached')
        obj = UserAgentTrack.objects.create(user_agent = user_agent , count = 1)
        count = obj.count

    D['count'] = count
    D['user_agent'] = user_agent
    return render(request, 'user_agent/index.html', D)
