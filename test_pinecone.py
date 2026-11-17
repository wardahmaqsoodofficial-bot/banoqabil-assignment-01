
import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("PINECONE_API_KEY")

# Check API key
if not api_key:
    raise ValueError("Pinecone API key not found!")

# Connect to Pinecone
pc = Pinecone(api_key=api_key)

# Test connection
print("Pinecone client initialized!")

# Verify connection by listing indexes
print(pc.list_indexes())
