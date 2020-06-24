
from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

class MyFirstSkill(Skill):
    '''My first test skill using github for opsdroid'''

    @match_regex('how are you?')
    async def how_are_you(self, message):
        await message.respond("Good thanks!, How are you sir")

