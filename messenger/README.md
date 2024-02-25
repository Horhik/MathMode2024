# Flask Messenger

## How to install it

Just execute `install.sh` and `run.sh`

### With Nix or in NixOS

Just run `nix-shell shell.nix`
Then execute `flask --app minimal run --debug`

### On Windows

Open terminal in project folder

```

pip install -r requirements.txt
flask --app minimal run --debug

```

## How to use it

1) Open browser at http://127.0.0.1:5000

2) You'll see login screen

3) Log in or Register

You can go into "Pool" 

It's public chat for all users

Or type username and if such user exsists you'l start chat with that person

## Using the bot Orwell

Send `\commands` into chat to see avaliable options


# Small Documentation

## Database

messenger database is just a filetree

```bash
users
├── oleg
│   └── messages
│       └── ne_oleg.chat 
└── ne_oleg
    └── messages
        └── oleg.chat 
```




## Structure of `.chat`

Each line of file conatins one-line json

The first line contains info about chat
`{"name": string, "participants": [string]}`

Other lines are messages
`{"time": int, "sender": string, "text": string}`

## TODO
- [x] Public pool of messages
- [x] Simple 2-person chat
- [x] Auto update
- [ ] Basic security
- [ ] API
