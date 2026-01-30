# Import all needed outside info
import os, argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import system_prompt
from call_function import available_functions, call_function

def main():
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

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    generate_content(client, messages, args.verbose)

def generate_content(client, messages, verbose: bool):

    # The actual generation of content
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0,
            tools=[available_functions],)
    )

    # Code block regarding token usage
    if response.usage_metadata is None:
        raise RuntimeError("No usage metadata!")

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    # Printing the results
    if verbose:
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if response.function_calls is not None:
        function_results = []
        for f in response.function_calls:
        #    print(f"Calling function: {f.name}({f.args})")
            function_call_result = call_function(f)
            if function_call_result.parts is None:
                raise Exception("Error: Empty .parts list!")
            
            if function_call_result.parts[0].function_response is None:
                raise Exception("Error: How did you manage that?")
            
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Error: The function did not return a response")
            
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

            function_results.append(function_call_result.parts[0])

    else:
        print(response.text)

if __name__ == "__main__":
    main()