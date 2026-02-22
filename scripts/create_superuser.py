import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

def create_superuser():
    print("Creating superuser...")
    # Add your superuser creation logic here
    print("Superuser created successfully!")

if __name__ == "__main__":
    create_superuser()
