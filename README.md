# Postman API Counter

### How to use
- Download `postman.py`
- Run this to count the API
```bash
python postman.py ~/path/to/postman_collection.json
# Total API: 57
```
- Show available folder
```bash
python postman.py ~/path/to/postman_collection.json -l
# User
# Business
# Order
# Product

python postman.py ~/path/to/postman_collection.json User -l
# Auth
# General

python postman.py ~/path/to/postman_collection.json User.General -l
# OTP
# Message
```
- To count spesific folder
```bash
python postman.py ~/path/to/postman_collection.json User
# Total API: 24

python postman.py ~/path/to/postman_collection.json User.General
# Total API: 10

python postman.py ~/path/to/postman_collection.json User.General.OTP
# Total API: 2
```
- Help menu
```bash
python postman.py -h
```