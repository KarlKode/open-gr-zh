from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.models import Meeting, AgendaItem, Speech

Meeting_Pydantic = pydantic_model_creator(Meeting, name="Meeting")
MeetingIn_Pydantic = pydantic_model_creator(
    Meeting, name="MeetingIn", exclude_readonly=True
)
MeetingList_Pydantic = pydantic_queryset_creator(Meeting)

AgendaItem_Pydantic = pydantic_model_creator(AgendaItem, name="AgendaItem")
AgendaItemIn_Pydantic = pydantic_model_creator(
    AgendaItem, name="AgendaItemIn", exclude_readonly=True
)
AgendaItemList_Pydantic = pydantic_queryset_creator(AgendaItem, allow_cycles=True)

Speech_Pydantic = pydantic_model_creator(Speech, name="Speech")
SpeechIn_Pydantic = pydantic_model_creator(
    Speech, name="SpeechIn", exclude_readonly=True
)
SpeechList_Pydantic = pydantic_queryset_creator(Speech)
