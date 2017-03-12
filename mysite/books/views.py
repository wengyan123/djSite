from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book, Publisher
from books.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import ListView



# Create your views here.
def display_meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            print("null")
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                          {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})


class PublisherList(ListView):
    model = Publisher
