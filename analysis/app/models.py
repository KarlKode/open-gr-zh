from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Meeting(models.Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    number = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    # agenda_items: fields.ReverseRelation["Speech"]

    class Meta:
        table = "meetings"
        unique_together = [("date", "number")]

    class PydanticMeta:
        pass


class AgendaItem(models.Model):
    id = fields.IntField(pk=True)
    gr_number = fields.CharField(max_length=10, null=True, index=True)
    meeting = fields.ForeignKeyField("models.Meeting", related_name="agenda_items")
    meeting_ordering = fields.SmallIntField()
    parent = fields.ForeignKeyField(
        "models.AgendaItem", related_name="children", null=True
    )
    title = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    speeches: fields.ReverseRelation["Speech"]
    children: fields.ReverseRelation["AgendaItem"]

    class Meta:
        table = "agenda_items"
        unique_together = [("meeting_id", "meeting_ordering")]
        indexes = [("gr_number", "meeting_id", "title")]

    class PydanticMeta:
        pass


class CouncilMember(models.Model):
    # id = fields.UUIDField(pk=True)
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, index=True)
    party = fields.CharField(max_length=100, index=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    speeches: fields.ReverseRelation["Speech"]

    def __str__(self):
        return self.name

    class Meta:
        table = "council_members"
        unique_together = [("name", "party")]
        indexes = [("name", "party")]

    class PydanticMeta:
        pass


class Speech(models.Model):
    id = fields.IntField(pk=True)
    council_member = fields.ForeignKeyField(
        "models.CouncilMember", related_name="speeches"
    )
    item = fields.ForeignKeyField("models.AgendaItem", related_name="speeches")
    item_ordering = fields.SmallIntField()
    mp3_url = fields.TextField()
    mp3_path = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "speeches"
        unique_together = [("item_id", "item_ordering")]
        indexes = [("council_member_id", "item_id")]

    class PydanticMeta:
        pass


Meeting_Pydantic = pydantic_model_creator(Meeting, name="Meeting")
MeetingIn_Pydantic = pydantic_model_creator(
    Meeting, name="MeetingIn", exclude_readonly=True
)
AgendaItem_Pydantic = pydantic_model_creator(AgendaItem, name="AgendaItem")
AgendaItemIn_Pydantic = pydantic_model_creator(
    AgendaItem, name="AgendaItem", exclude_readonly=True
)
CouncilMember_Pydantic = pydantic_model_creator(CouncilMember, name="CouncilMember")
CouncilMemberIn_Pydantic = pydantic_model_creator(
    CouncilMember, name="CouncilMemberIn", exclude_readonly=True
)
Speech_Pydantic = pydantic_model_creator(Speech, name="Speech")
SpeechIn_Pydantic = pydantic_model_creator(
    Speech, name="SpeechIn", exclude_readonly=True
)
