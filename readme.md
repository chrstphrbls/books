# Book Store app
- this is based on the Django for beginners pdf
```link
https://github.com/chrstphrbls/books
```

## added features
```link
      https://github.com/users/chrstphrbls/projects/1/views/1
```
- User Registration
- Pages App
 -installed docker
- PostgreSQL Database
- Advanced User Registration
- Environment Variables

## bugs
- nav bar bug - lis is not supposed to be in the left side of the nav bar.accordion-button
- bug upon clicking signup button, can create
```
AttributeError at /accounts/signup/
'tuple' object has no attribute 'rsplit'
Request Method:	POST
Request URL:	http://127.0.0.1:8000/accounts/signup/
```


## fixed bugs

- cannot log Out after logging in. -fixed by removing the excess tag inside the LogOut button. `type="button"` into `type="submit"`

- bug upon clicking login button
```
ModuleNotFoundError at /accounts/login/
No module named 'allauth.accounts'
Request Method:	POST
Request URL:	http://127.0.0.1:8000/accounts/login/
``` fixed by adding the allauth_socialaccounts in the settings.py


```html
      href="{% url 'acccount_signup' %}">Sign Up</a>
```fixed by adding the allauth_socialaccounts in the settings.py


- crispy forms cannot be used. 
```bash
Warning: Python 3.10 was not found on your system...
Neither 'pyenv' nor 'asdf' could be found to install Python.
You can specify specific versions of Python with:
$ pipenv --python path/to/python
```
- python version cannot be found on your system... - fixed by editing the Pipfile 3.10 into 3.7

## QA Comments
Current issues found:  
- QAs installing docker/dependencies

## Contributing QAs
-[@christophernabo](https://github.com/christophernabo)  
-[@MaFloresTuscano](https://github.com/MaFloresTuscano)

