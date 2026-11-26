from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def load_prompt(name: str, version: str, **kwargs) -> str:
    """Reads a versioned prompt file and fills in template variables."""
    prompt_path = BASE_DIR / "prompts" / f"{name}_{version}.txt"
    
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
        
    template = prompt_path.read_text(encoding="utf-8")
    return template.format(**kwargs)

if __name__ == "__main__":
    sample_ticket = "My password reset link expired and I can't log in."
    
    prompt_v1 = load_prompt("classifier", "v1", ticket=sample_ticket)
    prompt_v2 = load_prompt("classifier", "v2", ticket=sample_ticket)
    
    print("--- V1 PROMPT ---")
    print(prompt_v1)
    print("\n--- V2 PROMPT ---")
    print(prompt_v2)
