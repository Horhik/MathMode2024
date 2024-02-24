# Flask Messenger

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



# Small Documentation

## Structure of `.chat`

Each line of file conatins one-line json

The first line contains info about chat
`{"name": string, "participants": [string]}`

Other lines are messages
`{"time": int, "sender": string, "text": string}`

## TODO
- [x] Public pool of messages
- [ ] Simple 2-person chat
- [x] Auto update
- [ ] Basic security
- [ ] API
