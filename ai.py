import streamlit as st
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

api_key = st.secrets['OPENAI_SECRET']
client = OpenAI(api_key = api_key)


def story_generator(prompt):
    story_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            'system',
            "content":
            """You are bestseller story writer. You will take user's prompt and generate a 100 words short story for adults age 20-30"""
        }, {
            "role": 'user',
            "content": f'{prompt}'
        }],
        max_tokens=400,
        temperature=0.8)

    return story_response


def design_generator(prompt):
    design_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role":
            'system',
            "content":
            """Based on the story given. You will design a detailed image prompt for the cover image of this story.
              The image prompt should include the theme of the story with relevant color, suitable for adults.
              The output should be within 100 characters.
              """
        }, {
            "role": 'user',
            "content": f'{prompt}'
        }],
        max_tokens=400,
        temperature=0.8)

    return design_response


def create_image(prompt):
    cover_response = client.images.generate(
        model="dall-e-2",
        prompt=f"{prompt}",
        size="256x256",
        quality="standard",
        n=1  #1 output from it
    )

    image_url = cover_response.data[0].url

    return image_url


prompt = """Write a scary story on a little boy getting stucked in the woods, there are silouhettes and scary figures looming behind him. Show the ghost or scary figure behind him"""


def generate_story(prompt):
    story_response = story_generator(prompt).choices[0].message.content
    design_response = design_generator(
        story_response).choices[0].message.content
    image_url = create_image(design_response)

    return image_url


# response = requests.get(image_url)

# img = Image.open(BytesIO(response.content))
# img
