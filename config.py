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
keyboard_tokens = ["<0>","<1>","<2>","<3>","<4>",
                   "<5>","<6>","<7>","<8>","<9>"]
special_tokens: dict = {"additional_special_tokens":action_tokens+keyboard_tokens}

WHITELIST = {
	"ServerList": {
		744554485350924408: {
			"Name": "Elle's Server",
            "Channels": {
				744554485350924411: 
                    {"Name":"General",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server": 744554485350924408},
                869292497359220777:
                    {"Name":"Stocks",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 744554485350924408}
			},

		},
        937022042732126269: {
			"Name": 'DnD & Chill',
            "Channels": {
				1079472916900626484:
                    {"Name":"Ask Emme",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server": 937022042732126269},
                 937047094370373642:
                    {"Name":"Off Topic",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 937022042732126269},
                938494804797587486:
                    {"Name":"Duel Monsters",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 937022042732126269},
                937122411592179813:
                    {"Name":"General",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 937022042732126269},
                944334178873401395:
                    {"Name":"Dungeonz n Dragoonz Memez",
                    "Type":"Channel",
                    "Reply":False,
                    "ResponseChance": 0.05,
                    "Server": 937022042732126269}
			}

		},
        633239257213042699: {
            "Name": "Kotario's World",
            "Channels": {
				633239258185990169:
                {"Name":"banter",
                 "Type":"Channel",
                 "Reply":False,
                 "ResponseChance": 0.05,
                 "Server": 633239257213042699}
        }
	    },
        1018154248988540939: {
        "Name": "Rocky Rose's server",
        "Channels": {
			1018159343394357298:
            {"Name":"general chat",
             "Type":"Channel",
             "Reply":False,
             "ResponseChance": 0.05,
             "Server": 1018154248988540939}
        }
	    },
        940420353136664636: {
        "Name": "Moment's Trading",
        "Channels": {
			940421740385935391:
            {"Name":"Trading Floor",
             "Type":"Channel",
             "Reply":False,
             "ResponseChance": 0.05,
             "Server": 940420353136664636}
        }
	    },
	},

	"UserList": {166947533879377920:
                    {"Name":"Elle",
                    "Type":"DM",
                    "Reply":False,
                    "ResponseChance": 1,
                    "Server":0}
	}
}
config = Config()