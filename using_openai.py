"""Content Completion"""
from typing import List, Union

import openai
from fastapi import APIRouter
from pydantic import BaseModel, Field


router = APIRouter()


class TextCompletion(BaseModel):

    """Content generation payload"""

    api_key: str
    prompt: str = None
    model: str = Field(default="text-davinci-003")
    temperature: Union[int, None] = Field(default=0)
    max_tokens: Union[int, None] = Field(default=100)
    top_p: Union[int, None] = Field(default=1)
    frequency_penalty: Union[int, None] = Field(default=0)
    presence_penalty: Union[int, None] = Field(default=0)


class UsageData(BaseModel):
    """Usage response"""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChoiceData(BaseModel):
    """Choice data"""
    text: str
    index: int
    logprobs: str = None
    finish_reason: str


class TextCompletionResponse(BaseModel):
    """Response data"""
    id: str
    object: str
    created: int
    model: str
    choices: List[ChoiceData]
    usage: UsageData


@router.post("/text", response_model=TextCompletionResponse)
def get_text_results(payload: TextCompletion):
    """ Text completion service
    Args:
        item (TextCompletion): BaseModel class used to define necessary fields
    Returns:
        _type_: JSON
    """
    sample_apikey = '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'

    openai.api_key = payload.api_key

    # Prepare payload for OpenAI content generation
    response = openai.Completion.create(
        model=payload.model,
        prompt=payload.prompt,
        temperature=payload.temperature,
        max_tokens=payload.max_tokens,
        top_p=payload.top_p,
        frequency_penalty=payload.frequency_penalty,
        presence_penalty=payload.presence_penalty
    )

    # Response will contain how many tokens we have used for current search
    # To get remaining tokens and usage history, we have to goo through usage details in website
    # We will get results based on how many tokens we give in input and openai model

    return response
