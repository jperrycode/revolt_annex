# models.py
from django.db import models

class ParentModel(models.Model):
    date_field = models.DateField()
    # Other fields of the parent model

class ChildModel(models.Model):
    parent_model = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
    # Other fields of the child model





# views.py
from django.views.generic.dates import YearArchiveView
from .models import ParentModel

class ParentModelYearArchiveView(YearArchiveView):
    model = ParentModel
    date_field = 'date_field'
    make_object_list = True
    allow_future = True
    template_name = 'your_template.html'



<!-- your_template.html -->
<h2>{{ year }} Archive</h2>
<ul>
    {% for object in object_list %}
        <li>{{ object.date_field }} - {{ object.some_other_field }}</li>
    {% endfor %}
</ul>
