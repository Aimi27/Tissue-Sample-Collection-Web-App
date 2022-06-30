import os
import secrets
from flask import render_template, url_for, flash, redirect, request, abort
from flaskwebapp import app, db
from flaskwebapp.forms import CollectionForm, SampleForm
from flaskwebapp.models import User, Post, Collections, Samples

# Home page function
@app.route("/")
@app.route("/home") #2nd route
def home():
	collections = Collections.query.all()
	return render_template('home.html', collections=collections)

# About page function
@app.route("/about")
def about():
    return render_template('about.html')
	
# create route for new collection
@app.route("/collections/new", methods=['GET', 'POST'])
def new_collection():
	form = CollectionForm()
	if form.validate_on_submit():
		collection = Collections(disease_term=form.disease_term.data, title=form.title.data)
		db.session.add(collection)
		db.session.commit()
		flash('Your collection has been created!', 'success')
		return redirect(url_for('home'))
	return render_template('create_collection.html', title='New Collection', form=form)
	
# create route for new sample
@app.route("/samples/new", methods=['GET', 'POST'])
def new_sample():
	form = SampleForm()
	if form.validate_on_submit():
		flash('Your sample has been created!', 'success')
		return redirect(url_for('home'))
	return render_template('create_sample.html', title='New Sample', form=form)
	
# create route for a collection
@app.route("/collections/<int:collections_id>")
def collection(collections_id):
    collection = Collections.query.get_or_404(collections_id)
    return render_template('collection.html', title=collection.title, collection=collection)