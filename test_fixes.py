#!/usr/bin/env python3
"""
Test script to verify the article detection fixes
"""

import stanza
import sys
import importlib.util

# Load the module with space in filename
spec = importlib.util.spec_from_file_location("example_1", "example 1.py")
example_1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example_1)

EnhancedComplexityTracker = example_1.EnhancedComplexityTracker

def test_article_detection():
    print("Testing article detection fixes...")
    
    # Initialize the tracker (this will download models if not available)
    print("Initializing tracker...")
    try:
        tracker = EnhancedComplexityTracker()
    except Exception as e:
        print(f"Error initializing tracker: {e}")
        print("Attempting to download Stanza models...")
        stanza.download('la')
        stanza.download('es') 
        tracker = EnhancedComplexityTracker()
    
    # Test Latin text (should show 0 articles)
    latin_text = "Caesar Galliam vicit. Omnes viros fortes laudat."
    print("\n=== Testing Latin Text ===")
    print(f"Text: {latin_text}")
    
    latin_results = tracker.analyze_function_words(latin_text, 'la')
    print(f"Total articles found: {latin_results['total_by_type']['articles']}")
    print(f"Word count: {latin_results['word_count']}")
    print(f"Articles by type: {dict(latin_results['articles'])}")
    
    # Test Spanish text (should show actual articles)
    spanish_text = "El rey conquistó la ciudad. Los soldados son valientes."
    print("\n=== Testing Spanish Text ===")
    print(f"Text: {spanish_text}")
    
    spanish_results = tracker.analyze_function_words(spanish_text, 'es')
    print(f"Total articles found: {spanish_results['total_by_type']['articles']}")
    print(f"Word count: {spanish_results['word_count']}")
    print(f"Articles by type: {dict(spanish_results['articles'])}")
    
    # Test article rate calculation
    print("\n=== Testing Rate Calculation ===")
    if spanish_results['word_count'] > 0:
        total_articles = spanish_results['total_by_type']['articles']
        rate_per_1000 = (total_articles / spanish_results['word_count']) * 1000
        print(f"Article rate per 1000 words: {rate_per_1000:.2f}")
    
    print("\n=== Test Results ===")
    print(f"✓ Latin articles (should be 0): {latin_results['total_by_type']['articles']}")
    print(f"✓ Spanish articles (should be >0): {spanish_results['total_by_type']['articles']}")
    print("Test completed!")

if __name__ == "__main__":
    test_article_detection()