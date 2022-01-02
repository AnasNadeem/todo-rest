# Todo API
Its a todo application with authentication and stuffs.

### How to run this project:
### Prequisite
* You should have Python installed on your Machine.
Now Open Terminal or Shell.

### Steps:
1. ``` python -m pip install requirements.txt ```
2. ``` python manage.py runserver ```


## Endpoints:

### Main urls 
``` 
path('mainadmin/', admin.site.urls),
path('api/auth/', include('authentication.urls')),
path('api/', include('todoapp.urls')),
path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
```

### Authentication urls 
``` 
path('register', RegisterAPiView.as_view()),
path('login', LoginApiView.as_view()),
```

### TodosList urls 
``` 
path('todoslist/', TodosListApiView.as_view()),
path('todoslist/<int:pk>', TodosListDetailApiView.as_view()),
path('todoslistall/<int:pk>', TodosListBriefView.as_view()),
```

### Todos urls 
``` 
path('todos/', TodosApiView.as_view()),
path('todos/<int:pk>', TodosDetailApiView.as_view())
```

## Enjoy :)