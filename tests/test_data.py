import json

only_root = json.loads(
    """
    {
      "id": "a",
      "location": "A_1:15",
      "name": "root",
      "selectionText": "",
      "storyText": "lorem ipsum",
      "choices": []
    }
    """
)

simple_tree = json.loads(
    """
    {
    "id": "b",
    "location": "A_1:15",
    "name": "root",
    "selectionText": "",
    "storyText": "lorem ipsum",
    "choices": [
        {
        "id": "c",
        "name": "boop",
        "selectionText": "select me!",
        "storyText": "sloop",
        "choices": []
        },
        {
        "id": "e",
        "name": "snoop",
        "selectionText": "no, select me!",
        "storyText": "gloop",
        "choices": []
        }
    ]
    }
    """
)

complex_tree = json.loads(
    """
    {
    "id": "f",
    "location": "A_1:15",
    "name": "root",
    "selectionText": "",
    "storyText": "lorem ipsum",
    "choices": [
        {
        "id": "g",
        "name": "boop",
        "selectionText": "boop central",
        "storyText": "sloop",
        "choices": [
            {
            "id": "h",
            "name": "blob",
            "selectionText": "blob factory",
            "storyText": "gandalf the wizard",
            "choices": [
                {
                "id": "i",
                "name": "hobbit",
                "selectionText": "hairy feet",
                "storyText": "short",
                "choices": [
                    {
                    "id": "j",
                    "name": "dwarf",
                    "selectionText": "hairy face",
                    "storyText": "hairy",
                    "choices": [
                        {
                        "id": "k",
                        "name": "elf",
                        "selectionText": "hairy head",
                        "storyText": "pointy",
                        "choices": [
                            {
                            "id": "l",
                            "name": "orc",
                            "selectionText": "hairy chest",
                            "storyText": "smelly",
                            "choices": [
                                {
                                "id": "m",
                                "name": "human",
                                "selectionText": "hairy ears",
                                "storyText": "normy",
                                "choices": []
                                }
                            ]
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            },
            {
            "id": "n",
            "name": "goof",
            "selectionText": "goof central",
            "storyText": "spoof",
            "choices": []
            },
            {
            "id": "o",
            "name": "silly",
            "selectionText": "rabbit central",
            "storyText": "rabbit",
            "choices": [
                {
                "id": "p",
                "name": "tricks",
                "selectionText": "this one?",
                "storyText": "yum",
                "choices": []
                },
                {
                "id": "q",
                "name": "are for",
                "selectionText": "or this one?",
                "storyText": "bum",
                "choices": []
                },
                {
                "id": "r",
                "name": "kids",
                "selectionText": "or maybe this one?",
                "storyText": "tum",
                "choices": []
                }
            ]
            }
        ]
        },
        {
        "id": "s",
        "name": "snoop",
        "selectionText": "snoopy?",
        "storyText": "gloop",
        "choices": []
        },
        {
        "id": "t",
        "name": "flop",
        "selectionText": "flippy?",
        "storyText": "bop",
        "choices": [
            {
            "id": "u",
            "name": "groob",
            "selectionText": "groobly",
            "storyText": "snoob",
            "choices": []
            },
            {
            "id": "v",
            "name": "tube",
            "selectionText": "toobly",
            "storyText": "scooby doo",
            "choices": [
                {
                "id": "w",
                "name": "Arthur",
                "selectionText": "Warthur",
                "storyText": "the rabbit",
                "choices": []
                }
            ]
            }
        ]
        }
    ]
    }
    """
)
