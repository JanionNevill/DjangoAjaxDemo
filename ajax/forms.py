from django.forms import Form, IntegerField


class FiobonacciForm(Form):
    index = IntegerField(min_value=1, max_value=1000)

    class Meta:
        method = "POST"
