import streamlit as st
from crewai import Agent, Task, Crew

st.title("Recipe Generator and Nutrition Analyzer")

# Input for the recipe prompt
recipe_prompt = st.text_area("Enter your recipe idea:")
button= st.button("Generate Recipe")

if button:
    if recipe_prompt:

        #Create agents for recipe generation
        chef = Agent(
            role="Chef",
            goal="Generate a delicious recipe based on the provided idea",
            backstory="This agent is a skilled chef with extensive knowledge of ingredients and cooking techniques. They will create mouth-watering recipes.",
            llm="ollama/llama3.2"
        )

        nutritionist = Agent(
            role="Nutritionist",
            goal="Analyze the nutritional value of the generated recipe",
            backstory="This agent is a certified nutritionist who can assess the health benefits and nutritional content of recipes. They will provide insights on dietary needs and health considerations.",
            llm="ollama/llama3.2"
        )

        # Create a task for the agents
        generate_recipe = Task(
            description=f"Generate a recipe based on the idea: {recipe_prompt}",
            expected_output="A detailed recipe with ingredients and instructions.",
            agent=chef
        )

        analyze_nutrition = Task(
            description="Analyze the nutritional value of the generated recipe",
            expected_output="A comprehensive nutritional analysis.",
            agent=nutritionist
        )

        # Create a crew to manage the agents and tasks
        recipe_crew = Crew(
            agents=[chef, nutritionist],
            tasks=[generate_recipe, analyze_nutrition]
        )

        # Kick off the recipe generation process
        final_recipe = recipe_crew.kickoff()

        # Display the generated recipe and nutrition analysis
        st.subheader("Generated Recipe")
        st.markdown(generate_recipe.output)  # Display the generated recipe

        st.subheader("Nutritional Analysis")
        st.markdown(final_recipe)  # Display the nutritional analysis