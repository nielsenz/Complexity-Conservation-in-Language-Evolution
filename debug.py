import stanza
from pathlib import Path
from collections import defaultdict
import json
from typing import Dict, List, Tuple
import pandas as pd

class CorpusDebugger:
    def __init__(self):
        self.latin_nlp = stanza.Pipeline('la')
        self.spanish_nlp = stanza.Pipeline('es')
        self.corpus_dir = Path("corpus")
        self.debug_results = defaultdict(dict)

    def load_sample_texts(self, sample_size: int = 1000) -> Dict[str, str]:
        """Load sample from each text for debugging"""
        samples = {}
        
        # Load samples from each period
        for period in ['classical_latin', 'medieval_latin', 'early_spanish']:
            dir_path = self.corpus_dir / period
            for text_file in dir_path.glob("*.txt"):
                with open(text_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    samples[f"{period}_{text_file.stem}"] = content[:sample_size]
        
        return samples

    def debug_verb_features(self, text: str, language: str) -> Dict:
        """Detailed analysis of verb forms and features"""
        nlp = self.latin_nlp if language == 'la' else self.spanish_nlp
        doc = nlp(text)
        
        verb_analysis = {
            'verb_count': 0,
            'aux_count': 0,
            'verb_features': defaultdict(int),
            'aux_patterns': [],
            'potential_constructions': []
        }
        
        for sent in doc.sentences:
            # Find all verbs and auxiliaries
            verbs = [w for w in sent.words if w.upos == 'VERB']
            auxiliaries = [w for w in sent.words if w.upos == 'AUX']
            
            verb_analysis['verb_count'] += len(verbs)
            verb_analysis['aux_count'] += len(auxiliaries)
            
            # Track verb features
            for verb in verbs:
                if verb.feats:
                    for feature in verb.feats.split('|'):
                        verb_analysis['verb_features'][feature] += 1
            
            # Look for potential analytical constructions
            if auxiliaries:
                for aux in auxiliaries:
                    context = sent.text
                    verb_analysis['aux_patterns'].append({
                        'auxiliary': aux.text,
                        'features': aux.feats,
                        'context': context
                    })
            
            # Check for specific medieval patterns
            if language == 'la':
                self._check_medieval_patterns(sent, verb_analysis)
        
        return verb_analysis

    def _check_medieval_patterns(self, sentence, analysis: Dict):
        """Special checks for medieval Latin patterns"""
        words = sentence.words
        
        # Look for emerging analytical patterns
        for i, word in enumerate(words):
            if word.upos == 'AUX' or word.upos == 'VERB':
                # Look ahead for participles or infinitives
                for next_word in words[i+1:i+4]:  # Check next 3 words
                    if next_word.upos == 'VERB':
                        if 'VerbForm=Part' in (next_word.feats or ''):
                            analysis['potential_constructions'].append({
                                'type': 'possible_analytical',
                                'pattern': f"{word.text} ... {next_word.text}",
                                'context': sentence.text
                            })

    def compare_across_periods(self, samples: Dict[str, str]) -> Dict:
        """Compare linguistic features across periods"""
        comparisons = defaultdict(list)
        
        for text_name, content in samples.items():
            period = text_name.split('_')[0]
            language = 'es' if period == 'early' else 'la'
            
            analysis = self.debug_verb_features(content, language)
            
            # Store key metrics
            comparisons['texts'].append(text_name)
            comparisons['verb_counts'].append(analysis['verb_count'])
            comparisons['aux_counts'].append(analysis['aux_count'])
            comparisons['synthetic_candidates'].append(
                len([f for f in analysis['verb_features'].keys() 
                     if 'Tense=' in f or 'Voice=Pass' in f])
            )
            comparisons['analytical_candidates'].append(
                len(analysis['potential_constructions'])
            )
        
        return dict(comparisons)

    def generate_debug_report(self) -> str:
        """Generate detailed debugging report"""
        samples = self.load_sample_texts()
        comparisons = self.compare_across_periods(samples)
        
        report = ["Corpus Debug Report", "=" * 50, "\n"]
        
        # Period comparisons
        report.append("Period Comparisons:")
        for i, text in enumerate(comparisons['texts']):
            report.append(f"\n{text}:")
            report.append(f"  Verbs found: {comparisons['verb_counts'][i]}")
            report.append(f"  Auxiliaries found: {comparisons['aux_counts'][i]}")
            report.append(f"  Synthetic candidates: {comparisons['synthetic_candidates'][i]}")
            report.append(f"  Analytical candidates: {comparisons['analytical_candidates'][i]}")
        
        # Detailed medieval analysis
        report.append("\nMedieval Text Analysis:")
        medieval_samples = {k:v for k,v in samples.items() if 'medieval' in k}
        for text_name, content in medieval_samples.items():
            analysis = self.debug_verb_features(content, 'la')
            report.append(f"\n{text_name}:")
            report.append("  Verb Features:")
            for feature, count in analysis['verb_features'].items():
                report.append(f"    {feature}: {count}")
            report.append("\n  Potential Analytical Constructions:")
            for const in analysis['potential_constructions'][:5]:  # Show first 5
                report.append(f"    Pattern: {const['pattern']}")
                report.append(f"    Context: {const['context'][:100]}...")
        
        return "\n".join(report)

    def save_debug_results(self, filename: str = "debug_results.json"):
        """Save debugging results to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.debug_results, f, indent=2)

if __name__ == "__main__":
    debugger = CorpusDebugger()
    print(debugger.generate_debug_report())