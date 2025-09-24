import os
import requests
from typing import Optional


def generate_llm_response(prompt: str, system: Optional[str] = None, max_tokens: int = 256) -> Optional[str]:
    """
    Generate response from a free LLM provider if configured.
    Currently supports Hugging Face Inference API (text-generation) with free tier.

    Returns None if provider is not configured or on error.
    """
    provider = os.environ.get('FREE_LLM_PROVIDER', '').upper()
    if provider not in {'HUGGINGFACE'}:
        return None

    hf_api_token = os.environ.get('HF_API_TOKEN')
    hf_model = os.environ.get('HF_MODEL', 'google/gemma-2-2b-it')
    if not hf_api_token:
        return None

    headers = {
        'Authorization': f'Bearer {hf_api_token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    # Simple prompt formatting for instruct models
    full_prompt = prompt if not system else f"System: {system}\n\nUser: {prompt}\nAssistant:"

    payload = {
        'inputs': full_prompt,
        'parameters': {
            'max_new_tokens': max_tokens,
            'temperature': 0.3,
            'top_p': 0.9,
            'return_full_text': False,
        }
    }

    try:
        resp = requests.post(
            f'https://api-inference.huggingface.co/models/{hf_model}',
            headers=headers,
            json=payload,
            timeout=30,
        )
        if resp.status_code != 200:
            return None
        data = resp.json()
        # HF returns list of candidates with 'generated_text'
        if isinstance(data, list) and data and 'generated_text' in data[0]:
            return data[0]['generated_text'].strip()
        # Some models return dict
        if isinstance(data, dict):
            generated = data.get('generated_text') or data.get('answer')
            if generated:
                return str(generated).strip()
    except Exception:
        return None

    return None


