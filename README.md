# Boot count

A tiny Flask app to count the number of times a container has booted.

## API endpoints

`/api/count/`

* `GET` requests return JSON of the current count `{"count": <int>}`
* `POST` requests increment the counter by 1

## Development

To build and run locally:

* Build: `docker build -t acmilabs/boot-count:v1 .`
* Run: `docker run -it -p 5000:5000 acmilabs/boot-count:v1`

You can visit the app in your browser at: http://localhost:5000

Test it by sending a `POST` request: `curl --location --request POST 'http://localhost:5000/api/count/'`
