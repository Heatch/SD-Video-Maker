from pydantic import BaseModel, Field
from typing import List
from openai import OpenAI
from prompt import prompt
from teststory import story

class Character(BaseModel):
    name: str
    type: str
    image_prompt: str = Field(..., description="Detailed prompt for generating a portrait image of the character's face")

class Scene(BaseModel):
    name: str
    story_text: str
    image_prompt: str = Field(..., description="Detailed prompt for generating an image of the scene")

class StoryResponse(BaseModel):
    characters: List[Character]
    scenes: List[Scene]

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": story},
    ],
    response_format={"type": "json_object"},
    max_tokens=15000,
)

message = completion.choices[0].message
print(message.content)
