import streamlit as st
from crewai import Crew, Process
from tools import yt_tools
from agents import *
from tasks import *
#from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound




st.title("Blog Generator")

# Topic input
topic = st.text_input("Enter the topic:")

def initialize_crew():
    return Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True
    )
# Generate Content button
if st.button("Generate Content"):
    if topic:
        # Initialize Crew inside the button click to ensure it only starts when needed
        crew = initialize_crew()
        with st.spinner("Generating content ..."):
            try:
                result = crew.kickoff(input={'topic': topic})
                st.success("Content generation successful!!")
                st.write(result)
            except Exception as e:
                st.error(f"Content generation failed. Error: {e}")
    else:
        st.warning("Please enter a topic before generating content.")


