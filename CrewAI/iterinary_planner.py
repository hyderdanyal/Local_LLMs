import streamlit as st
from crewai import Agent, Task, Crew

st.title("Travel Itinerary Planner with CrewAI")

# Input for the itinerary prompt
destination = st.text_input("Enter your travel destination:")
button= st.button("Plan trip")

if button:
    if destination:

        #Create agents for iterinary planning and local expert advice
        planner = Agent(
            role="Trip Planner",
            goal="Create a detailed travel itinerary for the specified destination",
            backstory="This agent is a seasoned travel planner with extensive knowledge of destinations and local attractions. They will create comprehensive itineraries.",
            llm="ollama/llama3.2"
        )

        local_expert = Agent(
            role="Local Expert",
            goal="Provide insights and recommendations about the specified destination",
            backstory="This agent is a local expert with in-depth knowledge of the destination's culture, attractions, and hidden gems. They will offer personalized advice for the traveler.",
            llm="ollama/llama3.2"
        )

        # Create a task for the agents
        create_itinerary = Task(
            description=f"Create a travel itinerary for {destination}",
            expected_output="A detailed iterinary including activities and timing.",
            agent=planner
        )

        get_local_insights = Task(
            description=f"Provide local insights about{destination}",
            expected_output="Recommendations for places to visit and eat.",
            agent=local_expert
        )

        # Create a crew to manage the agents and tasks
        itinerary_crew = Crew(
            agents=[planner, local_expert],
            tasks=[create_itinerary, get_local_insights]
        )


        # Kick off the recipe generation process
        final_iterinary = itinerary_crew.kickoff()

        # Display the generated recipe and nutrition analysis
        st.subheader("Generated Recipe")
        st.markdown(create_itinerary.output)  # Display the generated recipe

        st.subheader("Nutritional Analysis")
        st.markdown(final_iterinary)  # Display the nutritional analysis