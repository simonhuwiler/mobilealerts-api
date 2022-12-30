# Api-Proxys für Mobile Alerts Client
 Hier sind verschiedene Proxys, für das [Mobile Alerts-Dashboard-Projekt](https://github.com/simonhuwiler/mobilealerts-client). Eine Anleitung liegt im jeweiligen Verzeichnis.

 * [Python](python/)
 * [PHP](php/)
 * Node: Siehe [dieses Projekt](https://github.com/simonhuwiler/mobilealerts-client)

## Wieso braucht es einen Proxy?
Der Server kann nicht direkt angesprochen werden, weil einige Header-Angaben angepasst werden müssen. Die meisten Browser lassen es nicht zu, die Header-Angaben zu überschreiben.

## Einen eigenen Proxy schreiben
Die Funktionsweise ist einfach: Leite den Request an den Server weiter und ersetze den Header. Dein Request muss wie folgt aussehen:  

**Methode**  
```
POST
```


**URL**  
```
https://www.data199.com/api/v1/dashboard
```

**Headers**  
```
User-Agent: Dalvik/2.1.0 (Linux; U; Android 6.0; Android SDK built for x86 Build/MASTER)
Content-Type: application/x-www-form-urlencoded
Host: www.data199.com
```