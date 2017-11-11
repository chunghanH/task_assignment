def show_message(message_type='', text=''):
	# Argument
	# - message_type: green, blue, red, deep_blue, yellow
	# - text: any text 

	references = {
		'red' : 'bg-danger',
		'green' : 'bg-success',
		'blue' : 'bg-info',
		'yellow' : 'bg-warning',
		'deep_blue' : 'bg-primary',
		'' : '',
	}

	message = {
		'message' : {
			'message_type' : references[message_type], 
			'text' : text,
		}
	}

	return message