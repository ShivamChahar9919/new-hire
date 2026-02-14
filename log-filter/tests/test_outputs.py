import os
from pathlib import Path

def test_logic():
    # The absolute path inside the container
    output_file = Path("/app/errors.txt")
    
    if not output_file.exists():
        print("ERROR: Output file not found")
        exit(1)
        
    content = output_file.read_text().strip().split('\n')
    
    # Based on our input, we expect exactly 2 ERROR lines
    if len(content) == 2:
        print("Verification Successful")
        exit(0)
    else:
        print(f"ERROR: Expected 2 lines, got {len(content)}")
        exit(1)

if __name__ == "__main__":
    test_logic()
