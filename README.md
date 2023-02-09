# Noip telegram bot

  ## Require:
  - set environment variable:
  ```bash
  export BOT_TOKEN=<your bot telegram bot token>
  ```
  - Replace profile: resources/mapper.json

  example resources/mapper.json: 
  ```json
  [
    {
      "domain": "kubesphere.ddns.net",
      "username": "your account",
      "password": "your password"
    },
    {
      "domain": "proxym.ddns.net",
      "username": "your account",
      "password": "your password"
    },
    {
      "domain": "idp-server.ddns.net",
      "username": "your account",
      "password": "your password"
    },
    {
      "domain": "phpma.ddns.net",
      "username": "your account",
      "password": "your password"
    }
  ]
  ```
  ## Run by source code:
  ```bash
  pip install -r resources/r.txt &&\
  python main.py
  ```
  ## Run by docker:
  ```bash
  docker run -it \
  --restart always \
  --name noip-telegram-bot \
  -e BOT_TOKEN=5329867726:AAH-mkpyr7cQmWXx7k8pFel72bFyukV2sk0 \
  -v /your/path/to/mapper.json:/app/resources/mapper.json \
  baristi000/noip-telegram-bot:latest
  ```