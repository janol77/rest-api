#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager
from werkzeug import generate_password_hash
from app.db import db
from flask import Flask
from api.models.user import User
from api.models.task import Task
import os
import sys

users = [{'name': 'jperez',
          'email': 'jperez@example.com',
          'password': 'jperez'},
         {'name': 'amora',
          'email': 'amora@example.com',
          'password': 'amora'},
         {'name': 'jvargas',
          'email': 'jvargas@example.com',
          'password': 'jvargas'}]

tasks = [{'title': 'eat',
          'description': 'eat the food'},
         {'title': 'clean',
          'description': 'clean the clothes'},
         {'title': 'wash',
          'description': 'wash the dishes'}]


def create_app(config="config.ini"):
    app = Flask(__name__)
    app.config.from_object(__name__)
    if os.path.exists(config):
        app.config.from_pyfile(config)
    else:
        print("The app does not have a config.ini file")
    # Define the WSGI application object
    db.init_app(app)
    return app

app = create_app()
manager = Manager(app)


@manager.command
def init_db():
    """Inicializar la base de datos."""
    list_id = []
    for task in tasks:
        task_list = Task.objects.filter(title=task['title'])
        task_object = task_list.first()
        if not task_object:
            title = task['title']
            description = task['description']
            u = Task(title=title, description=description).save()
            list_id.append(u.id)
            print "Task id %s" % (u.id,)
        else:
            print "Tarea %s creada anteriormente." % (task['title'],)

    for user in users:
        users_list = User.objects.filter(email=user['email'])
        user_object = users_list.first()
        if not user_object:
            password = generate_password_hash(user['password'])
            email = user['email']
            name = user['name']
            u = User(email=email,
                     name=name,
                     password=password,
                     tasks=list_id).save()
            print "Usuario id %s" % (u.id,)
        else:
            print "Usuario %s creado anteriormente." % (user['name'],)


@manager.command
def clean_db():
    """Inicializar la base de datos."""
    valid = ['y', 'yes']
    sys.stdout.write(u"confirme eliminación de Usuarios: ")
    choice = raw_input().lower()
    if choice in valid:
        users_deleted = User.objects.delete()
        print "Usuarios Borrados %s" % (users_deleted)
    else:
        print "Cancelado"

    sys.stdout.write(u"confirme eliminación de Tareas: ")
    choice = raw_input().lower()
    if choice in valid:
        tasks_deleted = Task.objects.delete()
        print "Tareas Borradas %s" % (tasks_deleted)
    else:
        print "Cancelado"

if __name__ == "__main__":
    manager.run()
