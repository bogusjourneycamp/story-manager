import json

only_root = json.loads('''
{
  "location": "A_1:15",
  "name": "root",
  "text": "lorem ipsum",
  "choices": {}
}
''')

simple_tree = json.loads('''
{
  "location": "A_1:15",
  "name": "root",
  "text": "lorem ipsum",
  "choices": {
    "select me!": {
      "name": "boop",
      "text": "sloop",
      "choices": {}
    },
    "no, select me!": {
      "name": "snoop",
      "text": "gloop",
      "choices": {}
    }
  }
}
''')

complex_tree = json.loads('''
{
  "location": "A_1:15",
  "name": "root",
  "text": "lorem ipsum",
  "choices": {
    "boop central": {
      "name": "boop",
      "text": "sloop",
      "choices": {
        "blob factory": {
          "name": "blob",
          "text": "gandalf the wizard",
          "choices": {
            "hairy feet": {
              "name": "hobbit",
              "text": "short",
              "choices": {
                "hairy face": {
                  "name": "dwarf",
                  "text": "hairy",
                  "choices": {
                    "hairy head": {
                      "name": "elf",
                      "text": "pointy",
                      "choices": {
                        "hairy chest": {
                          "name": "orc",
                          "text": "smelly",
                          "choices": {
                            "hairy ears": {
                              "name": "human",
                              "text": "normy",
                              "choices": {}
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "goof central": {
          "name": "goof",
          "text": "spoof",
          "choices": {}
        },
        "rabbit central": {
          "name": "silly",
          "text": "rabbit",
          "choices": {
            "this one?": {
              "name": "tricks",
              "text": "yum",
              "choices": {}
            },
            "or this one?": {
              "name": "are for",
              "text": "bum",
              "choices": {}
            },
            "or maybe this one?": {
              "name": "kids",
              "text": "tum",
              "choices": {}
            }
          }
        }
      }
    },
    "snoopy?": {
      "name": "snoop",
      "text": "gloop",
      "choices": {}
    },
    "flippy?": {
      "name": "flop",
      "text": "bop",
      "choices": {
        "groobly": {
          "name": "groob",
          "text": "snoob",
          "choices": {}
        },
        "toobly": {
          "name": "tube",
          "text": "scooby doo",
          "choices": {
            "Warthur": {
              "name": "Arthur",
              "text": "the rabbit",
              "choices": {}
            }
          }
        }
      }
    }
  }
}
''')
