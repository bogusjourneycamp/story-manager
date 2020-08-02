import json

only_root = json.loads('''
{
  "location": "A_1:15",
  "name": "root",
  "text": "lorem ipsum",
  "choices": []
}
''')

simple_tree = json.loads('''
{
  "location": "A_1:15",
  "name": "root",
  "text": "lorem ipsum",
  "choices": [
    {
      "name": "boop",
      "text": "sloop",
      "choices": []
    },
    {
      "name": "snoop",
      "text": "gloop",
      "choices": []
    }
  ]
}
''')

complex_tree = json.loads('''
{
  "location": "A_1:15",
  "name": "root",
  "text": "lorem ipsum",
  "choices": [
    {
      "name": "boop",
      "text": "sloop",
      "choices": [
        {
          "name": "blob",
          "text": "gandalf the wizard",
          "choices": [
            {
              "name": "hobbit",
              "text": "short",
              "choices": [
                {
                  "name": "dwarf",
                  "text": "hairy",
                  "choices": [
                    {
                      "name": "elf",
                      "text": "pointy",
                      "choices": [
                        {
                          "name": "orc",
                          "text": "smelly",
                          "choices": [
                            {
                              "name": "human",
                              "text": "normy",
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
          "name": "goof",
          "text": "spoof",
          "choices": []
        },
        {
          "name": "silly",
          "text": "rabbit",
          "choices": [
            {
              "name": "tricks",
              "text": "yum",
              "choices": []
            },
            {
              "name": "are for",
              "text": "bum",
              "choices": []
            },
            {
              "name": "kids",
              "text": "tum",
              "choices": []
            }
          ]
        }
      ]
    },
    {
      "name": "snoop",
      "text": "gloop",
      "choices": []
    },
    {
      "name": "flop",
      "text": "bop",
      "choices": [
        {
          "name": "groob",
          "text": "snoob",
          "choices": []
        },
        {
          "name": "tube",
          "text": "scooby doo",
          "choices": [
            {
              "name": "Arthur",
              "text": "the rabbit",
              "choices": []
            }
          ]
        }
      ]
    }
  ]
}
''')