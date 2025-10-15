#!/usr/bin/env python3
"""
Detailed diagnostic of article detection across periods
"""

import sys
import importlib.util
import json
import numpy as np
from collections import defaultdict

# Load the module with space in filename
spec = importlib.util.spec_from_file_location("example_1", "example 1.py")
example_1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example_1)

EnhancedComplexityTracker = example_1.EnhancedComplexityTracker

def detailed_article_diagnosis():
    print("DETAILED ARTICLE DETECTION DIAGNOSIS")
    print("=" * 60)
    
    tracker = EnhancedComplexityTracker()
    corpus = tracker.load_corpus()
    
    # Let's examine what determiners are found in each period
    period_analysis = {
        'Classical Latin': [],
        'Medieval Latin': [],
        'Early Spanish': []
    }
    
    for text_name, text_content in corpus.items():
        # Determine period and language
        if text_name.startswith('latin_'):
            period = 'Classical Latin'
            language = 'la'
        elif text_name.startswith('medieval_'):
            period = 'Medieval Latin'
            language = 'la'
        elif text_name.startswith('spanish_'):
            period = 'Early Spanish'
            language = 'es'
        else:
            continue
        
        print(f"\n{'='*40}")
        print(f"ANALYZING: {text_name}")
        print(f"Period: {period}, Language: {language}")
        print(f"{'='*40}")
        
        # Process a sample of the text to see what's happening
        sample_text = text_content[:1000]  # First 1000 chars
        print(f"Text sample: {sample_text[:200]}...")
        
        # Get NLP processing
        nlp = tracker.latin_nlp if language == 'la' else tracker.spanish_nlp
        doc = nlp(sample_text)
        
        # Find all DET (determiner) tagged words
        all_determiners = []
        articles_counted = []
        
        for sent in doc.sentences:
            for word in sent.words:
                if word.upos == 'DET':
                    det_classification = tracker._classify_article(word, sent, language)
                    all_determiners.append({
                        'text': word.text,
                        'lemma': word.lemma,
                        'features': word.feats,
                        'classification': det_classification
                    })
                    
                    # Only count if not classified as 'not_article'
                    if det_classification != 'not_article':
                        articles_counted.append({
                            'text': word.text,
                            'classification': det_classification
                        })
        
        print(f"\nAll DET-tagged words found: {len(all_determiners)}")
        for det in all_determiners[:10]:  # Show first 10
            print(f"  '{det['text']}' (lemma: {det['lemma']}) -> {det['classification']}")
        if len(all_determiners) > 10:
            print(f"  ... and {len(all_determiners) - 10} more")
        
        print(f"\nActual articles counted: {len(articles_counted)}")
        for art in articles_counted[:10]:  # Show first 10
            print(f"  '{art['text']}' -> {art['classification']}")
        
        # Run full analysis
        full_results = tracker.analyze_function_words(text_content, language)
        total_articles = full_results['total_by_type']['articles']
        word_count = full_results['word_count']
        article_rate = (total_articles / word_count) * 1000 if word_count > 0 else 0
        
        print(f"\nFULL TEXT RESULTS:")
        print(f"  Total articles: {total_articles}")
        print(f"  Word count: {word_count}")
        print(f"  Article rate per 1000: {article_rate:.3f}")
        
        period_analysis[period].append({
            'text_name': text_name,
            'determiners_found': len(all_determiners),
            'articles_counted': total_articles,
            'word_count': word_count,
            'rate': article_rate,
            'sample_determiners': all_determiners[:5]
        })
    
    print(f"\n{'='*60}")
    print("SUMMARY BY PERIOD")
    print(f"{'='*60}")
    
    for period, analyses in period_analysis.items():
        if analyses:
            rates = [a['rate'] for a in analyses]
            print(f"\n{period}:")
            print(f"  Number of texts: {len(analyses)}")
            print(f"  Article rates: {[f'{r:.3f}' for r in rates]}")
            print(f"  Mean: {np.mean(rates):.3f}")
            print(f"  Std: {np.std(rates, ddof=1):.3f}")
            
            print(f"  Detailed breakdown:")
            for analysis in analyses:
                print(f"    {analysis['text_name']}: {analysis['determiners_found']} DET tags -> {analysis['articles_counted']} articles")
                if analysis['sample_determiners']:
                    sample_words = [d['text'] for d in analysis['sample_determiners']]
                    print(f"      Sample DET words: {sample_words}")
    
    return period_analysis

def compare_with_original_results():
    """Compare with the original flawed results"""
    print(f"\n{'='*60}")
    print("COMPARISON WITH ORIGINAL (FLAWED) RESULTS")
    print(f"{'='*60}")
    
    # These were the original false claims from the paper
    original_claims = {
        'Classical Latin': {'mean': 0.485, 'sd': 0.101, 'n': 7},
        'Medieval Latin': {'mean': 1.887, 'sd': 0.586, 'n': 5},
        'Early Spanish': {'mean': 0.858, 'sd': 0.166, 'n': 4}
    }
    
    print("\nORIGINAL (FLAWED) CLAIMS:")
    for period, stats in original_claims.items():
        print(f"  {period}: mean={stats['mean']}, sd={stats['sd']}, n={stats['n']}")
    
    print("\nWHY THESE WERE WRONG:")
    print("  1. Latin determiners (hic, ille, omnis, etc.) were incorrectly counted as articles")
    print("  2. Normalization used syntactic arguments instead of word counts")
    print("  3. No language-specific filtering was applied")

if __name__ == "__main__":
    analysis = detailed_article_diagnosis()
    compare_with_original_results()