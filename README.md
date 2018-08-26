Repo contains two modules:
1. feed_parser: simple RSS parser for currency exchanges.
2. currency_info_server: simple django app with endpoint for info about currency exchange values.
Install:
pip install -r requirements.txt or python setup.py develop (for development).
Then run migration in currency server:
python manage.py migrate

Running app:
Firstly run server (in currency_info_server directory: django manage.py runserver), couse feed parser communicate with server via api.
Then you can run parser: python parser.py in feed_parser directory. If you use specific ports, etc change settings.py in feed_parser.
TODO list:
add tests,
add authentication,
add more endpoints,
upgrade models with more data
