# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:49:06 2021

@author: carles
"""

from app import app, db, cli
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
