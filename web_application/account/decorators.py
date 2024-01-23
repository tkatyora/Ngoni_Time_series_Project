from django.shortcuts import redirect
#decorator that checks if the user is logged in
def unauthenticated_user(view_function):
    def wrapperfunc(request ,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_function(request , *args, **kwargs)
        
        return view_function
    return wrapperfunc 



