from django.shortcuts import render

from notifications.models import Notifications


# Create your views here.
def view_notifications(request):
    user = request.user
    notification = Notifications.objects.filter(receiver=user)

    for notif in notification:
        notif.message_read = True
        notif.save()

    return render(request, 'notifications/view_notifications.html', {'notifications': notification})
