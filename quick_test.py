#!/usr/bin/env python3
"""
Quick test to verify corrected article rate calculations
"""

import sys
import importlib.util
from pathlib import Path

# Load the module with space in filename
spec = importlib.util.spec_from_file_location("example_1", "example 1.py")
example_1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example_1)

EnhancedComplexityTracker = example_1.EnhancedComplexityTracker

def quick_corpus_test():
    print("Quick corpus test with corrected methodology...")
    
    tracker = EnhancedComplexityTracker()
    corpus = tracker.load_corpus()
    
    # Test a few representative texts
    test_texts = [
        ('latin_caesar_bg_1', 'la'),
        ('spanish_cid', 'es')
    ]
    
    article_results = {}
    
    for text_name, language in test_texts:
        if text_name not in corpus:
            print(f"Text {text_name} not found in corpus")
            continue
            
        print(f"\n=== Testing {text_name} ({language}) ===")
        text_content = corpus[text_name]
        
        # Sample first 500 chars for quick testing
        sample = text_content[:500]
        print(f"Text sample: {sample[:100]}...")
        
        results = tracker.analyze_function_words(sample, language)
        
        total_articles = results['total_by_type']['articles']
        word_count = results['word_count']
        article_rate = (total_articles / word_count) * 1000 if word_count > 0 else 0
        
        print(f"Articles found: {total_articles}")
        print(f"Word count: {word_count}")
        print(f"Article rate per 1000 words: {article_rate:.3f}")
        
        article_results[text_name] = {
            'language': language,
            'articles': total_articles,
            'words': word_count,
            'rate': article_rate
        }
    
    print("\n=== CORRECTED RESULTS SUMMARY ===")
    for text, data in article_results.items():
        print(f"{text}: {data['articles']} articles in {data['words']} words = {data['rate']:.3f} per 1000")
    
    return article_results

if __name__ == "__main__":
    quick_corpus_test()