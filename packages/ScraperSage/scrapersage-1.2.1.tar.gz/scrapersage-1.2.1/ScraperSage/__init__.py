"""
ScraperSage - A comprehensive web scraping and content summarization library with AI-powered features.

Supports multiple AI providers: Gemini, OpenAI, OpenRouter, and DeepSeek.
"""

from .scraper_sage import scrape_and_summarize
from .ai_providers import AIProviderFactory, get_api_key_for_provider

__version__ = "1.1.0"
__all__ = ["scrape_and_summarize", "AIProviderFactory", "get_api_key_for_provider"]