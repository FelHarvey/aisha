# Import all needed outside info
import os, argparse
from google.genai import types
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("No API key found")

client = genai.Client(api_key=api_key)

# Code block to allow user to imput prompts
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# Store a list of user prompts
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# The actual generation of content
response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages
)

# Code block regarding token usage
if response.usage_metadata is None:
    raise RuntimeError("No usage metadata!")

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

# Printing the results
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
print(response.text)