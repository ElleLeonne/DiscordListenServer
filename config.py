__version__ = 0.1

class Config:
    def __init__(self):
        self.context_window = 3
        self.temperature = 0.7
        self.length_penalty = 0.5
        self.reply_override = False
        self.whitelist = WHITELIST
    def change_temp(self, float):
        self.temperature = float
    def change_length_penalty(self, float):
        self.length_penalty = float
    def change_ctx_win(self, int):
        self.context_window = int
    def set_override(self, bool):
        self.reply_ovveride = bool

action_tokens = ["<|pass|>", "<|think|>"]
index_tokens = ["<0>","<1>","<2>","<3>","<4>",
                   "<5>","<6>","<7>","<8>","<9>"]
special_tokens: dict = {"additional_special_tokens":action_tokens+keyboard_tokens}

WHITELIST = {
	"ServerList": {
		0000000000000000: {
			"Name": "My Server",
            "Channels": {
				0000000000000000000: 
                    {"Name":"General",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server": 0000000000000},
                000000000000000000:
                    {"Name":"General 2",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 00000000000000000000}
			},

		},
        000000000000000: {
			"Name": 'DnD',
            "Channels": {
				00000000000000000000:
                    {"Name":"Things",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server": 00000000000000000},
                00000000000000000000:
                    {"Name":"Off Topic",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 0000000000000000000},
                0000000000000000000:
                    {"Name":"Duel Monsters",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 000000000000000000},
                0000000000000000000:
                    {"Name":"General",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 000000000000000000},
                00000000000000000:
                    {"Name":"Memez",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 00000000000000000}
			}

		},
        000000000000000000000000: {
            "Name": "World",
            "Channels": {
				00000000000000000:
                {"Name":"banter",
                 "Type":"Channel",
                 "Reply":False,
                 "ResponseChance": 0.05,
                 "Server": 0000000000000000000}
        }
	    },
        00000000000000000: {
        "Name": "server",
        "Channels": {
			00000000000000000000:
            {"Name":"general chat",
             "Type":"Channel",
             "Reply":False,
             "ResponseChance": 0.05,
             "Server": 000000000000000000}
        }
	    },
        0000000000000000000: {
        "Name": "Trading",
        "Channels": {
			000000000000000:
            {"Name":"Trading Floor",
             "Type":"Channel",
             "Reply":False,
             "ResponseChance": 0.05,
             "Server": 00000000000000000000}
        }
	    },
	},

	"UserList": {0000000000000000000:
                    {"Name":"Elle",
                    "Type":"DM",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server":0}
	}
}
config = Config()
