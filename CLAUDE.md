# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a computational linguistics research project that analyzes grammatical complexity evolution from Latin to Spanish. The project tests the "complexity conservation hypothesis" - that grammatical complexity redistributes rather than diminishes during language change.

## Key Architecture

### Core Components

- **corpus_downloader.py**: Downloads historical texts from online sources (Latin Library, Cervantes Virtual)
- **example 1.py**: Main analysis script using Stanza NLP for linguistic processing
- **debug.py**: Development debugging utilities

### Analysis Pipeline

1. **Text Collection**: Download Latin and Spanish texts from curated sources
2. **NLP Processing**: Uses Stanza pipelines for Latin ('la') and Spanish ('es') 
3. **Complexity Metrics**: Tracks analytical constructions, function words, dependency structures
4. **Statistical Analysis**: Non-parametric tests (Kruskal-Wallis, Mann-Whitney, Fisher's exact)

### Corpus Structure

```
corpus/
├── classical_latin/     # Caesar, Cicero, Livy, Sallust texts
├── medieval_latin/      # Gregory of Tours, Bede, Isidore texts  
├── early_spanish/       # Auto de los Reyes Magos, El Cid, Berceo, Fuero texts
└── modern_spanish/      # (placeholder for future expansion)
```

## Development Environment

### Python Dependencies

The project requires these key packages:
- `stanza` - NLP processing for Latin and Spanish
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `matplotlib` - Plotting
- `seaborn` - Statistical visualization
- `scipy` - Statistical tests
- `requests` - Web scraping
- `beautifulsoup4` - HTML parsing

### Setup Commands

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install stanza pandas numpy matplotlib seaborn scipy requests beautifulsoup4

# Download Stanza models
python -c "import stanza; stanza.download('la'); stanza.download('es')"
```

### Debugging and Development

```bash
# Run debugging analysis on text samples
python debug.py

# Debug specific corpus issues or NLP processing problems
```

## Running Analysis

### Primary Analysis Script

```bash
python "example 1.py"
```

This runs the complete corpus analysis pipeline:
1. Loads texts from corpus directory
2. Processes with Stanza NLP
3. Extracts complexity metrics
4. Performs statistical analysis
5. Generates detailed report

### Text Collection

```bash
python corpus_downloader.py
```

Downloads historical texts to populate the corpus directory.

## Key Research Findings (Corrected)

The analysis finds statistically significant evidence on two measures consistent with complexity conservation:

### Article Development (Kruskal–Wallis p = 0.0007)
- Classical Latin: mean 0.000 per 1000 words (95% CI: [0.000, 0.000])
- Medieval Latin: mean 0.000 per 1000 words (95% CI: [0.000, 0.000])
- Early Spanish: mean 107.018 per 1000 words (95% CI: [85.774, 122.359])

### Analytical Construction Shift (Fisher’s exact 2×2: Classical vs. Spanish, p = 0.0001)
- Classical Latin: 6,182 synthetic, 0 analytical
- Medieval Latin: 0/0 (model limitation; reported descriptively)
- Early Spanish: 0 synthetic, 22 analytical

### Dependency Complexity (Kruskal–Wallis p = 0.1140)
- Classical Latin: mean 3.973 depth (95% CI: [3.756, 4.174])
- Medieval Latin: mean 8.734 depth (95% CI: [4.803, 13.619])
- Early Spanish: mean 4.516 depth (95% CI: [3.339, 5.591])

Notes:
- Medieval analytical forms are underdetected by the Classical-trained Latin model; inference restricted to Classical↔Spanish for the categorical test.

### Display-Only Repository
- Distribution bundle (figures, tables, processed outputs) is mirrored at:
  - https://github.com/nielsenz/Complexity-Conservation-in-Language-Evolution-Display
  Use this for sharing/citation; main code remains in this repository.

## Important Notes

- Medieval Latin processing has limitations due to Stanza model training on Classical Latin
- The project uses non-parametric statistics due to small sample sizes typical in historical linguistics
- File paths must handle spaces (e.g. "example 1.py" requires quotes in commands)
- All texts are UTF-8 encoded
- The virtual environment `venv/` directory contains all dependencies and should be activated before running scripts

## Troubleshooting

### Common Issues

1. **Stanza Model Loading**: If models fail to load, ensure both 'la' and 'es' models are downloaded
2. **File Encoding**: All corpus texts expect UTF-8 encoding
3. **Memory Usage**: Full corpus analysis requires significant RAM due to NLP processing
4. **Statistical Warnings**: Non-parametric tests may produce warnings with small sample sizes - this is expected

## Research Context

This work contributes to historical linguistics by providing quantitative evidence for theoretical frameworks about language change, specifically challenging the assumption that languages necessarily simplify over time.
