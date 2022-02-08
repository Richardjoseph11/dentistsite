from django.shortcuts import render
from django.core.mail import send_mail

from .models import Category, Ourdentist, Testimony, Service, Appointment


def index(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_time = request.POST['your-time']
        your_schedule = request.POST['your-schedule']
        your_message = request.POST['your-message']
        data= Appointment(name=your_name,your_phone=your_phone,email=your_email,address=your_address,time=your_time,date=your_schedule,message=your_message)
        data.save()
        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_time': your_time,
            'your_schedule': your_schedule,
            'your_message': your_message,

        })
    category = Category.objects.all()
    testimony= Testimony.objects.all()
    ourdentist= Ourdentist.objects.all()
    context = {
        'category': category,
         'testimony': testimony,
        'ourdentist': ourdentist
    }
    return render(request,'index.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        #send mail
        send_mail(
            message_name, #subject
            message,      #message"
            message_email,   #sender's email
            ['richardjose1252@gmail.com'], #reciever's email
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def service(request):
    service = Service.objects.all()
    context = {
        'service': service
    }

    return render(request, 'service.html', context)

def about(request):
    ourdentist = Ourdentist.objects.all()
    context = {
        'ourdentist': ourdentist
    }
    return render(request, 'about.html', context)

def appointment(request):
    # if request.method == "POST":
    #     your_name = request.POST['your-name']
    #     your_phone = request.POST['your-phone']
    #     your_email = request.POST['your-email']
    #     your_address = request.POST['your-address']
    #     your_time = request.POST['your-time']
    #     your_schedule = request.POST['your-schedule']
    #     your_message = request.POST['your-message']
    #
    #     # #send mail
    #     # send_mail(
    #     #     message_name, #subject
    #     #     message,      #message"
    #     #     message_email,   #sender's email
    #     #     ['richardjose1252@gmail.com'], #reciever's email
    #     # )
    #     return render(request, 'appointment.html', {
    #         'your_name': your_name,
    #         'your_phone': your_phone,
    #         'your_email': your_email,
    #         'your_address': your_address,
    #         'your_time': your_time,
    #         'your_schedule': your_schedule,
    #         'your_message': your_message,
    #
    #         })
    # else:
        return render(request, 'index.html', {})

def pricing(request):
    category = Category.objects.all()
    context= {
        'category': category
    }
    return render(request, 'pricing.html',context)