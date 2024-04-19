# How to deploy the website with Traefik

1. Push le code sur Github

2. Se connecter au server, se rendre
```bash
/opt/charly/Site-web-lycee
```

3. Arrêter le siteweb précédant
Lister les containers `docker`
```bash
docker ps
```

Récupérer l'ID du container du site WEB, example `5d9db4b6aefe4`

Arrêter le container
```bash
docker rm -f <5d9db4b6aefe4>
```

Si le container s'arrête avec succès le terminal affiche l'ID

4. Pull le code du Github
```bash
git fetch && git pull
```

5. Reconstruire et démarer le container
```bash
docker compose up -d --build
```
