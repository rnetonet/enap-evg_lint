from django.views.generic import FormView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormView
from .forms import LinterForm
from linter_backend.robot import Robot

class IndexView(FormView, TemplateResponseMixin):
    template_name = 'linter_frontend/index.html'
    form_class = LinterForm
    
    def form_valid(self, form):
        cd = form.cleaned_data

        moodle_login_url = cd["moodle_login_url"]
        moodle_course_url = cd['moodle_course_url']
        login = cd['login']
        password = cd['password']
        
        report = []

        # login
        robot = Robot(login_url=moodle_login_url, login=login, password=password)
            
            

        return super().render_to_response(context={"form": form, "report": report})