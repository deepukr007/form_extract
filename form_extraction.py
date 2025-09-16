
from rich.pretty import pprint
from pydantic import BaseModel, Field
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.media import Image
from models_form import EinbuergerungsantragFormular

from dotenv import load_dotenv

load_dotenv()

form_extract_agent = Agent(
    model=OpenAIChat(id="gpt-5"),
    description="You will be given an image of a filled or blank form page in German. Your task is to detect all form fields (labels/keys) and extract their corresponding values. " \
    "Return a structured JSON object with clearly named keys and values. If a field is empty, return null or an empty value. For multiple-choice/check-box fields, " \
    "return which options are checked (true/false). Normalize dates to ISO format (YYYY-MM-DD) if present..",
    response_model=EinbuergerungsantragFormular,
    use_json_mode=True,
)

def run_form_extraction_agent(content: bytes) -> RunResponse:
    response = form_extract_agent.run(
        "Give me the structured output from the image",
        images=[
            Image(
                content=content
            )
        ],
        stream=False,
    )
    return response