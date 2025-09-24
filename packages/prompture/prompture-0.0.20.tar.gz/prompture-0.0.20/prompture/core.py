"""Core utilities: Helpers for requesting JSON from LLM.
"""
from __future__ import annotations
import json
import re
from typing import Any, Dict, Optional, Union

from .settings import settings
from .drivers import get_driver
from .driver import Driver


def clean_json_text(text: str) -> str:
    """Intentos básicos para extraer JSON si viene con ````` o explicaciones.
    No es perfecto; se recomienda usar prompts con ejemplos para forzar JSON válido.
    
    Also removes <think>...</think> blocks that might be present in LLM output.
    """
    # eliminar <think> blocks using regex
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    
    # eliminar fences ```json ``` o ```
    text = text.strip()
    # detect code fence and extract first code block
    if text.startswith("```"):
        # Find the first opening ```
        start_fence = text.find("```")
        if start_fence != -1:
            # Skip the opening fence and language tag
            start_content = text.find("\n", start_fence)
            if start_content != -1:
                # Find the first closing ```
                end_fence = text.find("```", start_content)
                if end_fence != -1:
                    # Extract content between fences
                    rest = text[start_content + 1:end_fence]
                    return rest.strip()
                else:
                    # No closing fence, take from start content to end
                    rest = text[start_content + 1:]
                    return rest.strip()
    # intentar extraer la primera ocurrencia de un objeto JSON
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return text[start:end+1]
    return text

def clean_json_text_with_ai(driver: Driver, text: str, options: Dict[str, Any] = {}) -> str:
    """Use LLM to fix malformed JSON strings.

    Creates a specialized prompt instructing the LLM to correct the provided text
    into a valid JSON object, then cleans the response to ensure no markdown fences remain.
    """
    prompt = (
        "The following text is supposed to be a single JSON object, but it is malformed. "
        "Please correct it and return only the valid JSON object. Do not add any explanations or markdown. "
        f"The text to correct is:\n\n{text}"
    )
    resp = driver.generate(prompt, options)
    raw = resp.get("text", "")
    cleaned = clean_json_text(raw)
    return cleaned

def ask_for_json(driver: Driver, content_prompt: str, json_schema: Dict[str, Any], ai_cleanup: bool = True, options: Dict[str, Any] = {}) -> Dict[str, Any]:
    """Sends a prompt to the driver and returns both JSON output and usage metadata.

    This function enforces a schema-first approach by requiring a json_schema parameter
    and automatically generating instructions for the LLM to return valid JSON matching the schema.

    Args:
        driver: adapter that implements generate(prompt, options)
        content_prompt: main prompt content (may include examples)
        json_schema: required JSON schema dictionary defining the expected structure
        ai_cleanup: whether to attempt AI-based cleanup if JSON parsing fails
        options: additional options to pass to the driver

    Returns:
        A dictionary containing:
        - json_string: the JSON string output
        - json_object: the parsed JSON object
        - usage: token usage and cost information from the driver's meta object
    """
    schema_string = json.dumps(json_schema, indent=2)
    instruct = (
        "Return only a single JSON object (no markdown, no extra text) that validates against this JSON schema:\n"
        f"{schema_string}\n\n"
        "If a value is unknown use null. Use double quotes for keys and strings."
    )
    full_prompt = f"{content_prompt}\n\n{instruct}"
    resp = driver.generate(full_prompt, options)
    raw = resp.get("text", "")
    cleaned = clean_json_text(raw)
    try:
        json_obj = json.loads(cleaned)
        return {
            "json_string": cleaned,
            "json_object": json_obj,
            "usage": resp.get("meta", {})
        }
    except json.JSONDecodeError:
        if ai_cleanup:
            # clean_json_text_with_ai returns just the cleaned string, so we need to get fresh metadata
            cleaned_fixed = clean_json_text_with_ai(driver, cleaned, options)
        try:
            json_obj = json.loads(cleaned_fixed)
            return {
                "json_string": cleaned_fixed,
                "json_object": json_obj,
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "cost": 0.0, "model_name": options.get("model", getattr(driver, "model", "")) }  # Model name from options or driver
            }
        except json.JSONDecodeError:
            raise
        
def extract_and_jsonify(
    driver: Driver,
    text: str,
    json_schema: Dict[str, Any],
    instruction_template: str = "Extract information from the following text:",
    ai_cleanup: bool = True,
    options: Dict[str, Any] = {}
) -> Dict[str, Any]:
    """Extracts structured information from text and returns it as a JSON object with usage metadata.

    This is a higher-level function that simplifies the process of extracting information
    into JSON by automatically constructing the content prompt and calling ask_for_json.

    Args:
        driver: The LLM driver instance to use for generation
        text: The raw text to extract information from
        json_schema: JSON schema dictionary defining the expected structure
        instruction_template: Template string for the extraction instruction
                          (default: "Extract information from the following text:")
        ai_cleanup: Whether to attempt AI-based cleanup if JSON parsing fails
        options: Additional options to pass to the driver

    Returns:
        A dictionary containing:
        - json_string: the JSON string output
        - json_object: the parsed JSON object
        - usage: token usage and cost information from the driver's meta object

    Raises:
        ValueError: If text is empty or None
        json.JSONDecodeError: If the response cannot be parsed as JSON and ai_cleanup is False

    Example:
        >>> schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        >>> result = extract_and_jsonify(driver, "John is a developer", schema)
        >>> result["json_string"]
        '{"name": "John"}'
        >>> result["usage"]["total_tokens"]
        150
    """
    if not text or not text.strip():
        raise ValueError("Text input cannot be empty")

    content_prompt = f"{instruction_template} {text}"
    return ask_for_json(driver, content_prompt, json_schema, ai_cleanup, options)

def auto_extract_and_jsonify(
    text: str,
    json_schema: Dict[str, Any],
    instruction_template: str = "Extract information from the following text:",
    ai_cleanup: bool = True,
    options: Dict[str, Any] = {}
) -> Dict[str, Any]:
    """Extracts structured information from text and returns it as a JSON object with usage metadata.
    
    This is a convenience function that automatically initializes the appropriate driver based on
    the AI_PROVIDER environment variable and uses it to extract structured information from text.
    It combines the functionality of get_driver() and extract_and_jsonify().

    Args:
        text: The raw text to extract information from
        json_schema: JSON schema dictionary defining the expected structure
        instruction_template: Template string for the extraction instruction
                          (default: "Extract information from the following text:")
        ai_cleanup: Whether to attempt AI-based cleanup if JSON parsing fails
        options: Additional options to pass to the driver

    Returns:
        A dictionary containing:
        - json_string: the JSON string output
        - json_object: the parsed JSON object
        - usage: token usage and cost information from the driver's meta object

    Raises:
        ValueError: If text is empty or None, or if driver initialization fails
        json.JSONDecodeError: If the response cannot be parsed as JSON and ai_cleanup is False

    Example:
        >>> schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        >>> result = auto_extract_and_jsonify("John is a developer", schema)
        >>> result["json_string"]
        '{"name": "John"}'
        >>> result["usage"]["total_tokens"]
        150
    """
    driver = get_driver()
    return extract_and_jsonify(
        driver=driver,
        text=text,
        json_schema=json_schema,
        instruction_template=instruction_template,
        ai_cleanup=ai_cleanup,
        options=options
    )