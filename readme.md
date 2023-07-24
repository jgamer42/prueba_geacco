# Technical test geacco
![python](https://img.shields.io/badge/-python%20-yellow?logo=python)
![django](https://img.shields.io/badge/-django%20-green?logo=django)
![docker](https://img.shields.io/badge/-Docker%20-grey?logo=docker)
![celery](https://img.shields.io/badge/-Celery%20-green?logo=celery)

## installation

## Domain concepts

- User: Anyone that hits the API , there is no restriction of any kind
- Document format: A file upload from an user that has a structure, it will be use as a template to fill the fields specified in them with {{}}
- Task: An specific process to do over a document format
- pipeline: An ordered list of task to do over a document format
## API
For quick test of this code here [postman collection](doc/postmant_collection.json) that you can import to postman, also here is a [tutorial](https://learning.postman.com/docs/collections/using-collections) about how to do it
### Database
![Database](doc/model.png)
### Queue and scheduling
![Scheduling model](doc/scheduling.jpg)
### Use cases
- As a user can upload a document template in PDF,Excel,Word or plain text
- As a user can fill a previous document template with his respective payload
- As a user can retrieve all the document templates in the system or an specific one
- As a user can create a pipeline of task for a document template
- As a user can retrieve the result of all pipeline or the result from specific step

## Steps forward
- Add unit tests
- set-up github actions

## Known bugs
- when replace fields on the template it still {} an after the change
- not always keeps the format of the document , specially with colors and images
- the bool values are not set in black on Excel files
