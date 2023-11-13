from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# Function to make API call to chat completion endpoint
def get_response(ai_role, user_request):
    client = OpenAI(api_key=OPENAI_API_KEY)

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": ai_role},
        {"role": "user", "content": user_request}
      ]
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    role= "You are a helpful assistant"
    request = "Tell me something to cheer me up"
    output = get_response(role, request)
    print(output)
