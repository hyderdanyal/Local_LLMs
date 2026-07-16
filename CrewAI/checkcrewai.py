import streamlit as st
from crewai import Agent, Task, Crew


st.title("CrewAI - Local LLM")

# Input for the prompt
prompt = st.text_area("Enter your prompt:")
button= st.button("Generate")

if button:
    if prompt:
        # Create an agent with role, goal, and backstory
        agent = Agent(
            role="Assistant", 
            goal="Provide helpful responses based on user input", 
            backstory="This agent assissts users by generating responses to their prompts using a local Ollama LLM.", 
            llm="ollama/llama3.2")

        # Create a task with the prompt
        task = Task(
            description=f"Generate a response based on user input: {prompt}",
            expected_output="The generated response will be a list",
            agent=agent # Assign the agent to the task
            )

        # Add the agent and task to the crew
        crew = Crew(agents=[agent], tasks=[task])

        # Generate a response using the crew
        result = crew.kickoff()

        # Display the response
        st.markdown("Result:")
        st.markdown(result)