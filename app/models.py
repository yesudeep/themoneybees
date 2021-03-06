#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; -*-
# Models for the datastore.
# Copyright (c) 2009 happychickoo.
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import configuration
from google.appengine.ext import db
from google.appengine.ext.db import polymodel
from google.appengine.api import memcache
#from haggoo.db.models import RegularModel

EMAIL_TYPE_CHOICES= (
        'personal',
        'office',
)

class profile(polymodel.PolyModel):
    pass
    
class person(profile):
    first_name = db.StringProperty(required=True)
    middle_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    when_born = db.DateProperty()

class EmailAddress(db.Model):
    email = db.EmailProperty()
    email_type = db.StringProperty(choices = EMAIL_TYPE_CHOICES)
    profile = db.ReferenceProperty(profile, collection_name='emails')


