from django.http import Http404, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin, FormView

from time import sleep

from .forms import FiobonacciForm


class HomeView(TemplateView):
    template_name = "ajax/home.html"


class ButtonDemoView(TemplateView):
    template_name = "ajax/btn_demo.html"


class FormDemoView(FormView):
    template_name = "ajax/form_demo.html"
    form_class = FiobonacciForm


class FibonacciPost(View):

    def post(self, request, *args, **kwargs):
        form = FiobonacciForm(self.request.POST)
        if not form.is_valid():
            raise Http404

        index = form.cleaned_data.get("index")
        fibonaccis = self._calculate_fibonacci_numbers(index)

        return JsonResponse(
            {
                "index": index,
                "number": fibonaccis[-1],
                "sequence": ", ".join([str(item) for item in fibonaccis]),
            }
        )

    @staticmethod
    def _calculate_fibonacci_numbers(index):
        sleep(1)
        numbers = [1, 1]
        while len(numbers) < index:
            numbers.append(sum(numbers[-2:]))

        return numbers[:index]
