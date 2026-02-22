import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

def reset_db():
    print("Resetting database...")
    # Add your database reset logic here
    print("Database reset successfully!")

if __name__ == "__main__":
    reset_db()
