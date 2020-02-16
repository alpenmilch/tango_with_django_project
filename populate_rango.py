import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page
def populate(): 
	 # First, we will create lists of dictionaries containing the pages 
	 # we want to add into each category.
	 # Then we will create a dictionary of dictionaries for our categories.
	 # This might seem a little bit confusing, but it allows us to iterate 
	 # through each data structure, and add the data to our models. 
 
	python_pages = [ 
		{'title': 'Official Python Tutorial', 
		'url':'http://docs.python.org/3/tutorial/',
		'views':111}, 
		{'title':'How to Think like a Computer Scientist',
		'url':'http://www.greenteapress.com/thinkpython/',
		'views':7},
		{'title':'Learn Python in 10 Minutes', 
		'url':'http://www.korokithakis.net/tutorials/python/',
		'views':10} ]
		
	django_pages = [
		{'title':'Official Django Tutorial',
		'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
		'views':42},
		{'title':'Django Rocks',
		'url':'http://www.djangorocks.com/',
		'views':13}, 
		{'title':'How to Tango with Django', 
		'url':'http://www.tangowithdjango.com/',
		'views':9} ]
		
	other_pages = [ 
		{'title':'Bottle', 
		'url':'http://bottlepy.org/docs/dev/',
		'views':12}, 
		{'title':'Flask', 
		'url':'http://flask.pocoo.org',
		'views':20} ]
		
	cats = {'Python': {'pages': python_pages, 'likes':64, 'views':128}, 
	'Django': {'pages': django_pages, 'likes':32, 'views':64}, 
	'Other Frameworks': {'pages': other_pages, 'likes':16, 'views':32} } 
	# If you want to add more categories or pages, 
	# add them to the dictionaries above. 
	# The code below goes through the cats dictionary, then adds each category, 
	# and then adds all the associated pages for that category. 
	for cat, cat_data in cats.items(): 
		c = add_cat(cat,cat_data['likes'],cat_data['views'])
		for p in cat_data['pages']:
			add_page(c, p['title'], p['url'], p['views'])
			
	# Print out the categories we have added. 
	for c in Category.objects.all(): 
		for p in Page.objects.filter(category=c):
			print(f'- {c}: {p}') 
				
def add_page(cat, title, url, views=0): 
	p = Page.objects.get_or_create(category=cat, title=title)[0] 
	p.url=url 
	p.views=views 
	p.save() 
	return p 
	
def add_cat(name,likes,views): 
	c = Category.objects.get_or_create(name=name)[0] 
	c.likes = likes
	c.views = views
	c.save() 
	return c
	
# Start execution here! 
if __name__ == '__main__': 
	print('Starting Rango population script...') 
	populate()