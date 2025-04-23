from crewai import Crew, Agent, Task, LLM
from pydantic import BaseModel
import yaml
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Load agents and tasks from yaml
def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

agents_config = load_yaml('agents.yaml')['agents']
tasks_config = load_yaml('tasks.yaml')['tasks']

# Define output schema
class BlogOutput(BaseModel):
    final_blog_markdown: str
    seo_score: float
    ai_score: float

# Create LLM with Groq using CrewAI's LLM class
llm = LLM(model="groq/meta-llama/llama-4-scout-17b-16e-instruct", api_key=api_key)

# Create agents
agents = {}
for name, cfg in agents_config.items():
    agents[name] = Agent(
        role=cfg['role'],
        goal=cfg['goal'],
        backstory=cfg['backstory'],
        llm=llm,
        verbose=True
    )

# Create tasks
tasks = {}
for name, cfg in tasks_config.items():
    if name == "orchestrate":
        tasks[name] = Task(
            description=cfg['description'],
            agent=agents[cfg['agent']],
            expected_output="Final Markdown blog with SEO and AI scores",
            output_model=BlogOutput
        )
    else:
        tasks[name] = Task(
            description=cfg['description'],
            agent=agents[cfg['agent']],
            expected_output="Intermediate content or evaluation"
        )

# Define the crew
crew = Crew(
    agents=list(agents.values()),
    tasks=list(tasks.values()),
    manager=agents['manager'],
    verbose=True
)

# Run the crew
if __name__ == "__main__":
    inputs = {
        'main_keyword': 'AI SEO techniques',
        'related_keywords': ['increase website visitors', 'AI content tools', 'SEO automation', 'low competition niches']
    }
    result = crew.kickoff(inputs=inputs)
