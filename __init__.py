__version__ = 0.1

WHITELIST = {
	"ServerList": {
		111111111111111111: {
			"Name": "Anon's Server",
            "Channels": {
				111111111111112: 
                    {"Name":"General",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server": 111111111111111111},
                111111111111113:
                    {"Name":"Jokes",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.1,
                    "Server": 111111111111111111}
			},

		},
        211111111111111111: {
			"Name": 'Duck Server',
            "Channels": {
				211111111111111112:
                {"Name":"Duck Channel",
                 "Type":"Channel",
                 "Reply":False,
                 "ResponseChance": 0.9,
                 "Server": 211111111111111111}
			}

		}
	},
	"UserList": {21212121212121121:
                    {"Name":"Me",
                    "Type":"DM",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server":0000000000}
	}
}

