from django.http import HttpResponse
from django.shortcuts import render


def contact(request):
    return HttpResponse(
        """
                        
                        
                        <h1>This is contact Page</h1>
                        <a href='/first_app/about/'>About</a>
                        
                        """
    )


def about(request):
    return HttpResponse(
        """
                        
                        
                        <h1>This is About Page</h1>
                        <a href='/first_app/about/'>Contact</a>
                        </br>
                        <a href='/second_app/courses/'>Courses</a>
                        
                        """
    )
