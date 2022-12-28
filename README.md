Anleitung: https://cloud.google.com/functions/docs/create-deploy-http-python

## Deploy
1. Mal:
```
gcloud init
```

```
gcloud functions deploy apiproxy --runtime python310 --trigger-http --allow-unauthenticated
```

## Call
https://us-central1-mobilealerts-372415.cloudfunctions.net/apiproxy

## Notizen
* https://github.com/levyitay/AddSecurityExceptionAndroid

## Run locally
1. Install functions-framework
```
pip install functions-framework
```

2. Run
```
functions_framework --target=apiproxy
```