import base64
your_string="import pygame as graphics\nimport os\nimport random\nimport csv\nimport pickle\nimport button\nfrom pygame import mixer\nos.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'"
sample_string_bytes = "import sys\nimport os\nos.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'\ndef blockPrint():\n\tsys.stdout = open(os.devnull, 'w')\nblockPrint()\nimport pygame as graphic\nimport button\nimport csv\nimport pickle".encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
your_string = base64_bytes.decode("ascii")
with open("graphic.bin","wb") as f:
    f.write(your_string.encode("utf-8"))