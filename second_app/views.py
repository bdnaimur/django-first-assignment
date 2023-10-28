from django.http import HttpResponse
from django.shortcuts import render


def courses(request):
    return HttpResponse(
        """
                        
                        
                        <h1>This is Courses Page</h1>
                        <a href='/second_app/feedback/'>feedback</a>
                        </br>
                        <a href='/first_app/about/'>About</a>
                        """
    )


def feedback(request):
    return HttpResponse(
        """
                        
                        
                        <h1>This is Courses Page</h1>
                        <a href='/second_app/courses/'>Courses</a>
                        
                        """
    )
