import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).parent.parent))

def seed():
    print("Seeding data...")
    # Add your seeding logic here
    print("Data seeded successfully!")

if __name__ == "__main__":
    seed()
