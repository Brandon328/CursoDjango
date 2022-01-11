django-admin startproject -nombreproyecto-

python3 manage.py runserver //para correr la aplicación 
python3 manage.py startapp -nombreapp- //para crear una app 
django-admin startapp -nombreapp- project\apps\-nombreapp-

python3 manage.py makemigrations //Va a buscar los cambios en nuestros modelos y los va a reflejar en un archivo.

python3 manage.py migrate //Va a aplicar esos cambios en nuestra base de datos.


python3 manage.py shell	


import pdb; pdb.set_trace() // para ejecutar un debugger en django
// mas aqui https://platzi.com/clases/1318-django/12403-el-objeto-request2427/


---

Dentro de /static/ se colocan archivos como videos, imagenes, css, js