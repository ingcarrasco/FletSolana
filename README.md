# Infra App

Desarrollada con flet

### Estructura inicial

```
|
|---| InfraApp
|---|---| assets
|---|---|---| assets/icon.png
|---|---| requirements.txt
|---|---| .gitignore
|---|---| main.py
|---|---| README.md
| compose.yml
| Dockerfile
| entrypoint.sh
| README.md
```

#### Carpeta InfraApp

Esta carpeta se creo con el template minimal

```sh
flet create --project InfraApp
```


```
docker compose up -d
```

```
flet run [app_directory]
```