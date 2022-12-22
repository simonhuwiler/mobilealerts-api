Anleitung: https://cloud.google.com/functions/docs/create-deploy-http-python

## Deploy
1. Mal:
```
gcloud init
```

```
gcloud functions deploy apiproxy --runtime python310 --trigger-http --allow-unauthenticated
```