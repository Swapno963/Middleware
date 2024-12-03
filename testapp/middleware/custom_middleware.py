from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Skip middleware logic for admin, login, and logout paths
        if request.path in [reverse('login'), reverse('logout'), reverse('admin:index')]:
            return
        
        # Check if the user is authenticated
        if request.user.is_authenticated:
            role = request.user.role
            print(role)

            # Define the home paths for each role
            role_home_paths = {
                'teacher': reverse('teacher_home'),
                'student': reverse('student_home'),
                'principal': reverse('principal_home'),
            }

            # Get the expected home path for the current role
            expected_home_path = role_home_paths.get(role)

            if expected_home_path and not request.path.startswith(expected_home_path):
                return redirect(expected_home_path)
