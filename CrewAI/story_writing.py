import streamlit as st
from crewai import Agent, Task, Crew

st.title("Story Writing with CrewAI")

# Input for the story prompt
story_prompt = st.text_area("Enter your story prompt:", height=300)
button= st.button("Generate Story")

if button:
    if story_prompt:

        #Create agents for story generation
        writer = Agent(
            role="Writer",
            goal="Generate a compelling story based on the provided prompt",
            backstory="This agent is skilled in creative writing and storytelling with a vivid imagination. They will craft engaging narratives.",
            llm="ollama/llama3.2"
        )

        editor = Agent(
            role="Editor",
            goal="Review and refine the story generated for clarity, coherence, and style",
            backstory="This agent is an experienced editor who ensures that the story is well-structured, clear, and engaging. They will provide constructive feedback.",
            llm="ollama/llama3.2"
        )

        # Create a task for the agents
        write_story = Task(
            description=f"Generate a story based on the prompt: {story_prompt}",
            expected_output="A creative short story with a beginning, middle, and end.",
            agent=writer
        )

        edit_story = Task(
            description="Review and refine the generated story for clarity, coherence, and style",
            expected_output="A polished and refined story",
            agent=editor
        )

        # Create a crew to manage the agents and tasks
        story_crew = Crew(
            agents=[writer, editor],
            tasks=[write_story, edit_story]
        )

        # Kick off the story generation process
        final_story = story_crew.kickoff()

        # Display the generated story
        # Create two columns for displaying the story and the editor's feedback
        col1, col2 = st.columns(2)

        # Input for the first column (generated story)
        with col1:
            st.subheader("First Story")
            st.markdown(write_story.output)  

        # Input for the second column (editor's feedback)
        with col2:
            st.subheader("Editor's Feedback")
            st.markdown(final_story)  # Display the final story after editing

        
