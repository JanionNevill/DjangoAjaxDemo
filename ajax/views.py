from django.http import Http404, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin, FormView
from django.utils import log

from time import sleep

from .forms import FiobonacciForm


def _calculate_fibonacci_numbers(index):
    sleep(2)
    numbers = [1, 1]
    while len(numbers) < index:
        numbers.append(sum(numbers[-2:]))

    return numbers[:index]


class HomeView(TemplateView):
    template_name = "ajax/home.html"


class ButtonDemoView(View):

    def get(self, request, *args, **kwargs):
        view = ButtonDemoGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ButtonDemoPost.as_view()
        return view(request, *args, **kwargs)


class ButtonDemoGet(TemplateView):
    template_name = "ajax/btn_demo.html"


class ButtonDemoPost(View):

    def post(self, request, *args, **kwargs):
        index = int(request.POST["index"])
        fibonaccis = _calculate_fibonacci_numbers(index)

        return JsonResponse(
            {
                "index": index,
                "number": fibonaccis[-1],
                "sequence": ", ".join([str(item) for item in fibonaccis]),
            }
        )


class FormDemoView(View):

    def get(self, request, *args, **kwargs):
        view = FormDemoGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = FormDemoPost.as_view()
        return view(request, *args, **kwargs)


class FormDemoGet(FormView):
    template_name = "ajax/form_demo.html"
    form_class = FiobonacciForm


class FormDemoPost(FormMixin, View):
    form_class = FiobonacciForm

    def post(self, request, *args, **kwargs):
        form = FiobonacciForm(self.request.POST)
        if not form.is_valid():
            raise Http404

        index = form.cleaned_data.get("index")
        fibonaccis = _calculate_fibonacci_numbers(index)

        return JsonResponse(
            {
                "index": index,
                "number": fibonaccis[-1],
                "sequence": ", ".join([str(item) for item in fibonaccis]),
            }
        )
