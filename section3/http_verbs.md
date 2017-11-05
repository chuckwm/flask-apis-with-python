# what we send when going to web server
GET / HTTP/1.1
Host: www.google.com

POST
DELETE
PUT
OPTIONS
HEAD
etc

verb           Meaning                               Example
GET          Retrieve something              GET /item/1
POST        Receive data, and                 POST /item  often json { 'name': 'Chair', 'price': 9.99 }
                use it
PUT           Make sure something            PUT /item often jason { 'name': 'Chair', 'price': 7.99 }
                  is there
DELETE    Remove something
