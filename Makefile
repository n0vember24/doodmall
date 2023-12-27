mgr:
	python3 manage.py makemigrations
	python3 manage.py migrate


mkmgr:
	python3 manage.py makemigrations

mkgr:
	python3 manage.py migrate

run:
	python3 manage.py run localhost:8000