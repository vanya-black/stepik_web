def wsgi_app (env, start_response):
	body = env['QUERY_STRING'].split('&')
	status = '200 OK'
	headers = [('Content-Type','text/plain')]
	start_response(status, headers)
	return(body)
	## pull test

