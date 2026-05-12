"""
LangChain Chain Examples with Memory Types

CHAINS in LangChain:
- A Chain is a sequence of components (prompts, LLMs, tools) linked together
- Chains orchestrate multiple steps: prompt -> LLM -> parsing -> tools
- They enable complex workflows by chaining operations

MEMORY TYPES in LangChain:
1. ConversationBufferMemory: Stores all messages (full history)
2. ConversationSummaryMemory: Summarizes conversation over time
3. ConversationBufferWindowMemory: Keeps only last N messages
4. ConversationEntityMemory: Tracks specific entities and their details
5. ConversationKGMemory: Uses knowledge graph for entity relationships
"""

import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_classic.chains import LLMChain, SequentialChain, SimpleSequentialChain
from langchain_classic.output_parsers import CommaSeparatedListOutputParser



# Initialize the LLM
llm = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-3-flash-preview")

# ============================================================================
# EXAMPLE 1: Simple Chain with PromptTemplate (No Memory)
# ============================================================================
print("=" * 70)
print("EXAMPLE 1: Simple Chain with PromptTemplate")
print("=" * 70)

# Create a prompt template with variables
template = """You are a helpful assistant.
Answer the following question about {topic}:
{question}
Provide a detailed answer."""

prompt_template = PromptTemplate(
    input_variables=["topic", "question"],
    template=template
)

# Get variables from command line or use defaults
topic ="history"
question = "What year did the first man land on the moon?"

# Format the prompt with variables
formatted_prompt = prompt_template.format(topic=topic, question=question)

# Invoke the chain
response = llm.invoke(formatted_prompt)
print(f"Topic: {topic}")
print(f"Question: {question}")
print(f"Response: {response}")
print()

# ============================================================================
# EXAMPLE 2: Multi-turn Conversation Simulation
# ============================================================================
print("=" * 70)
print("EXAMPLE 2: Multi-turn Conversation (Manual Memory Management)")
print("=" * 70)

# Simulate multi-turn conversation with manual history tracking
conversation_history = []

def chat(user_input):
    """Simulate conversation with history tracking"""
    # Add user message to history
    conversation_history.append(f"User: {user_input}")
    
    # Create context from history
    context = "\n".join(conversation_history[-4:])  # Keep last 4 messages
    
    # Create prompt with context
    chat_prompt = PromptTemplate(
        input_variables=["context", "user_input"],
        template="Conversation history:\n{context}\n\nRespond to: {user_input}"
    )
    
    prompt_text = chat_prompt.format(context=context, user_input=user_input)
    response = llm.invoke(prompt_text)
    
    # Add assistant response to history
    conversation_history.append(f"Assistant: {response}")
    return response

# Multi-turn conversation
print("\nTurn 1:")
r1 = chat("My name is John and I love AI")
print(f"Response: {r1}\n")

print("Turn 2:")
r2 = chat("What is my name?")
print(f"Response: {r2}\n")

print("Turn 3:")
r3 = chat("What do I love?")
print(f"Response: {r3}\n")

print("Conversation History:")
for msg in conversation_history:
    print(msg)
print()


# ============================================================================
# EXAMPLE 3: LLM Chain with Explicit Prompts
# ============================================================================
print("=" * 70)
print("EXAMPLE 3: LLM Chain (Direct Prompt to LLM)")
print("=" * 70)

# Direct invocation (simplest form of chain)
direct_prompt = "Explain quantum computing in simple terms"
print(f"Prompt: {direct_prompt}")
response = llm.invoke(direct_prompt)
print(f"Response: {response}")
print()

# ============================================================================
# EXAMPLE 4: LLMChain - Prompt + LLM Binding
# ============================================================================
print("=" * 70)
print("EXAMPLE 5: LLMChain (Binding Prompt to LLM)")
print("=" * 70)


# Create a prompt template
prompt_5 = PromptTemplate(
    input_variables=["product"],
    template="Write a creative marketing tagline for {product}"
)

# Create an LLMChain by binding the prompt and LLM
chain = LLMChain(llm=llm, prompt=prompt_5)

# Run the chain with input variables
result = chain.run(product="a sustainable water bottle")
print(f"Product: water bottle")
print(f"Tagline: {result}")
print()

# ============================================================================
# EXAMPLE 5: SequentialChain - Multiple Steps
# ============================================================================
print("=" * 70)
print("EXAMPLE 5: SequentialChain (Multiple Sequential Steps)")
print("=" * 70)

# Create first prompt and chain
prompt_6a = PromptTemplate(
    input_variables=["city"],
    template="Generate 3 tourist attractions in {city}"
)
chain_6a = LLMChain(llm=llm, prompt=prompt_6a, output_key="attractions")

# Create second prompt and chain (uses output from first chain)
prompt_6b = PromptTemplate(
    input_variables=["attractions"],
    template="Based on these attractions: {attractions}\nCreate a 2-day itinerary"
)
chain_6b = LLMChain(llm=llm, prompt=prompt_6b, output_key="itinerary")

# Create a sequential chain that combines both
overall_chain = SequentialChain(
    chains=[chain_6a, chain_6b],
    input_variables=["city"],
    output_variables=["attractions", "itinerary"],
    verbose=True
)

result = overall_chain({"city": "Paris"})
print(f"\nCity: Paris")
print(f"Attractions: {result['attractions']}")
print(f"Itinerary: {result['itinerary']}")
print()

# ============================================================================
# EXAMPLE 6: SimpleSequentialChain - Chain Multiple LLMs
# ============================================================================
print("=" * 70)
print("EXAMPLE 6: SimpleSequentialChain (Pass Output to Next LLM)")
print("=" * 70)

# Create prompts for sequential processing
prompt_7a = PromptTemplate(
    input_variables=["input"],
    template="Summarize this topic in 2 sentences: {input}"
)
chain_7a = LLMChain(llm=llm, prompt=prompt_7a)

prompt_7b = PromptTemplate(
    input_variables=["input"],
    template="Translate this to French: {input}"
)
chain_7b = LLMChain(llm=llm, prompt=prompt_7b)

# Create simple sequential chain (output of one is input to next)
simple_seq_chain = SimpleSequentialChain(
    chains=[chain_7a, chain_7b],
    verbose=True
)

result = simple_seq_chain.run("Artificial Intelligence and Machine Learning")
print(f"Final Result (Translated Summary): {result}")
print()

# ============================================================================
# EXAMPLE 7: Chain with Custom Output Parsing
# ============================================================================
print("=" * 70)
print("EXAMPLE 7: Chain with Output Parsing (Structured Data)")
print("=" * 70)

# Create an output parser
output_parser = CommaSeparatedListOutputParser()

# Create prompt that instructs LLM to output comma-separated values
prompt_8 = PromptTemplate(
    input_variables=["topic"],
    template="List 5 key concepts about {topic}. Return as comma-separated values.\n{format_instructions}",
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

chain_8 = LLMChain(llm=llm, prompt=prompt_8)

result = chain_8.run(topic="Machine Learning")
# Parse the comma-separated output into a list
concepts = output_parser.parse(result)
print(f"Topic: Machine Learning")
print(f"Concepts: {concepts}")
print()

# ============================================================================
# SUMMARY OF CHAIN TYPES
# ============================================================================
print("=" * 70)
print("SUMMARY OF CHAIN TYPES IN LANGCHAIN")
print("=" * 70)
print("""
1. LLMChain: 
   - Simplest chain: Prompt + LLM
   - Use when: Single step with template variables
   
2. ConversationChain:
   - Adds memory to track conversation history
   - Use when: Multi-turn conversations needed
   
3. SequentialChain:
   - Chains multiple operations in sequence
   - Passes outputs from one step to next
   - Use when: Complex workflows with dependencies
   
4. SimpleSequentialChain:
   - Simpler version of SequentialChain
   - Output of one chain becomes input to next
   - Use when: Sequential processing without multiple I/O
   
5. RouterChain:
   - Routes input to different chains based on conditions
   - Use when: Conditional processing needed
   
6. RetrievalQA Chain:
   - Combines retrieval with QA
   - Use when: Question answering over documents
   
7. OutputParser Chains:
   - Parses LLM output into structured formats
   - Use when: Need List, JSON, Rules output
""")
