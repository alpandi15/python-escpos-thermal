# Getting started!

## Before Started

1. run `sudo pip3 install virtualenv`
2. run `python3 -m venv virtualenv`
3. run `source virtualenv/bin/activate`
4. run `pip3 install -r requirements.txt`

## API ROUTE
- GET  `/check-connection?ip={ip_thermal}`
- POST  `/print?ip={ip_thermal}`

**Body**
```
{
    image: <base64>
}
```
