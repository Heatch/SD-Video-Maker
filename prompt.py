prompt = """Your job is to create a JSON output for a given story containing:

Characters:

name: The character's name
type: Specification of if the chartacter is human, animal, mystical creature, etc.
image_prompt: A detailed prompt for generating a portrait image of the character's face only, suitable for image generation models. Focus on human characters only, ignoring non-human ones.


Scenes:

name: The name of the primary character in the scene
story_text: The specific text from the story associated with this scene
image_prompt: A detailed prompt for generating an image of that scene, suitable for image generation models.
Rules/Guidelines for Scenes:

- Create an image prompt for every significant moment in the story, as if for a picture book.
- Each scene must focus on only one character. If multiple characters are involved, create separate scene entries for each character's perspective or creatively focus on one character at a time.
- Avoid including plot points in the character portrait prompts.
- Use imagination to fill in visual details not explicitly stated in the story.
- Ensure prompts are optimized for image generation, with clear descriptions of facial expressions, body language, and settings.
- Keep in mind that for image generation each prompt does not have context of the story, so redescription of the character and scene is necessary and no need to include the character's name in the prompt.
"""