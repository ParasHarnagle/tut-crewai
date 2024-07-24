import os
from crewai import Agent
from tools import yt_tools
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

blog_researcher = Agent(
    role = "Blog researcher from youtube videos",
    goal = "get relevent video content for the topic{topic} from yt channel",
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI, data science, machine lerning and GEN AI"
    ),
    tools = [yt_tools],
    allow_delegation = True
)

blog_writer = Agent(
    role = "Writer",
    goal = "Narrate compelling tech stories about the video{topic} from yt channel",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplyfying compex topics you craft engaging narrative that"
        "capitvates and educate the reader."
    ),
    tools = [yt_tools],
    allow_delegation = False
)