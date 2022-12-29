# Python (Google Cloud Functions) Api Proxy

Version in Python für Google Cloud Functions. Weitere Informationen, wie Cloud Functions eingerichtet werden kann, hier: https://cloud.google.com/functions/docs/create-deploy-http-python

## Installieren
``` 
pip install -r requirements.txt
```

## Deploy
Vorbereiten:
```
gcloud init
```

Deployen:
```
gcloud functions deploy apiproxy --runtime python310 --trigger-http --allow-unauthenticated
```
## Local ausführen
1. Install functions-framework
```
pip install functions-framework
```

2. Run
```
functions_framework --target=apiproxy
```