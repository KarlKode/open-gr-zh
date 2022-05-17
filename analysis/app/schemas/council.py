from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.models import CouncilMember

CouncilMember_Pydantic = pydantic_model_creator(CouncilMember, name="CouncilMember")
CouncilMemberIn_Pydantic = pydantic_model_creator(
    CouncilMember, name="CouncilMemberIn", exclude_readonly=True
)
CouncilMemberList_Pydantic = pydantic_queryset_creator(CouncilMember)
