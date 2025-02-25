To run this

install anaconda 

pip install -r requitements.txt

python manage.py makemigrations

python manage.py mirgate

python manage.py runserver

curl -X POST http://127.0.0.1:8000/api/chat/ -H "Content-Type: application/json" -d '{"message": "Hello, chatbot!"}'
