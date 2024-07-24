from crewai import Task
from tools import yt_tools
from agents import *

#research_ task
research_task = Task(
    description = (
        "Identify the topic{topic}."
        "get detailed information about the video from the channel"

    ),
    expected_output = "A comphrehensive 3 paragraph long report based on the {topic} of the video content",
    tools = [yt_tools],
    agent = blog_researcher

)

#writing task
write_task = Task(
    description = (
        "get info from youtube channel on the topic{topic}"
    ),
    expected_output = "summerise the info from the youtube channel video on the topic{topic} and create content for the blog",
    tools = [yt_tools],
    output_file = 'new_blog_post.md'
        
)