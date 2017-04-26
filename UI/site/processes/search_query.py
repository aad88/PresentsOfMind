# native imports

# project imports
import database, interests_form

# external imports


def process_query(user_id, info):
	# grab the information pieces provided
	q_label = info['label']
	q_age = info['age']
	q_gender = info['gender']
	q_hometown = info['hometown']
	q_interests = info['interests']
	
	# create a record of this search query
	database.create_search(user_id, q_label)
	
	# TODO: MACHINE LEARNING IMPLEMENTATION HERE
	
	# TODO: AMAZON SEARCH IMPLEMENTATION HERE
	gift_ideas = []
	
	# enter each resulting gift idea into the database
	for idea in gift_ideas:
		# enter as new gift idea, if applicable
		#TODO
		
		# enter in connection to this search
		#TODO
		pass

def process_manual_query(user_id, form):
	info = interests_form.info_from_form(form)
	
	process_query(user_id, info)

