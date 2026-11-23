import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Ensure API keys are set (e.g., OPENAI_API_KEY, SERPER_API_KEY)
search_tool = SerperDevTool()

# 1. Define Agents
researcher = Agent(
    role="Senior Technical Researcher",
    goal="Uncover groundbreaking developments in {topic}",
    backstory="You are an expert analyst known for finding accurate, primary-source data.",
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Write a concise, engaging technical brief about {topic}",
    backstory="You translate complex technical findings into clear, actionable insights.",
    verbose=True
)

# 2. Define Tasks
research_task = Task(
    description="Identify the top 3 trends and key challenges in {topic} for 2026.",
    expected_output="A bulleted list of 3 trends with supporting facts and sources.",
    agent=researcher
)

write_task = Task(
    description="Using the research findings, write a 3-paragraph summary.",
    expected_output="A polished 3-paragraph markdown brief.",
    agent=writer,
    context=[research_task]  # Explicitly passes output from research_task
)

# 3. Assemble and Kickoff
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

result = crew.kickoff(inputs={"topic": "Local LLM Inference Optimization"})
print(result)
