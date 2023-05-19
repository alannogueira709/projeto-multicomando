import json
from composeActs import Composer

with open("presentation.json") as file:
    presentation = json.load(file)
    composer = Composer(presentation, presentation["length"])
    
    composer.execute()
