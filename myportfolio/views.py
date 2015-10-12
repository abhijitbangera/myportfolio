from django.shortcuts import render,redirect
from myportfolio.forms import ContactForm

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core.mail import send_mail


def about(request):
	form_class = ContactForm
	context={"name":"Abhijit Bangera",
			"subtitle":"Programmer",
			'form': form_class
			}

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
		    subject = form.cleaned_data['subject']
		    message = form.cleaned_data['message']
		    sender = form.cleaned_data['sender']
		    cc_myself = form.cleaned_data['cc_myself']
		    recipients = ['abhijit.bangera@hotmail.com']
		    if cc_myself:
		        recipients.append(sender)
		    print(subject)
		    print(message)
		    print(sender)
		    print(recipients)

		    send_mail(subject, message, sender, recipients)

		    return redirect('/')





	return render(request, "index.html", context)



# add to your views
