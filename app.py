# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_punyrest():
	return (
		'Welcome to punyRest!\n'
		'You can use the follow comands:\n'
		'/help - get info about punyREST API methods\n'
		'/encode - encode follow domain to punycode\n'
		'/decode - decode follow domain from punycode\n'
	)


@app.route('/help')
def get_info():
	return (
		'Usage:\n'
		'/help - get info about punyREST API methods\n'
		'/encode - encode follow domain to punycode\n'
		'/decode - decode follow domain from punycode\n'
	)

@app.route('/encode/<domain>')
def encode_domain(domain):
	return domain.encode('idna') + '\n'


@app.route('/decode/<domain>')
def decode_domain(domain):
	return domain.decode('idna') + '\n'


if __name__ == '__main__':
	app.run()
