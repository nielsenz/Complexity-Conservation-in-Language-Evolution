# Grammatical Complexity Conservation in Indo-European Languages

A computational linguistics research project analyzing the evolution of grammatical complexity from Latin to Spanish, testing the hypothesis that complexity redistributes rather than diminishes during language change.

## Research Question

**"Does grammatical complexity in Indo-European languages redistribute rather than diminish during language change, maintaining a relatively constant 'complexity budget' across different grammatical subsystems?"**

## Key Findings

Our computational analysis provides **preliminary quantitative evidence** supporting the complexity conservation hypothesis, with two of three measures showing statistically significant changes:

### 1. Article Development (p=0.0007) ✅ SIGNIFICANT
- **Classical Latin**: No articles (mean 0.000 per 1000 words)
- **Medieval Latin**: No articles (mean 0.000 per 1000 words) 
- **Spanish**: Robust article system (mean 107.018 per 1000 words)
- **Conclusion**: Spanish developed articles to compensate for lost Latin case markings

### 2. Analytical Construction Shift (p=0.0001) ✅ SIGNIFICANT
- **Classical Latin**: Exclusively synthetic constructions (6,182 instances)
- **Medieval Latin**: Transitional period (0 instances detected - NLP limitation)
- **Spanish**: Clear shift toward analytical constructions (22 instances)
- **Conclusion**: Complete structural transition from synthetic to analytical forms

### 3. Dependency Complexity Evolution (p=0.1140) ⚠️ NON-SIGNIFICANT
- **Classical Latin**: Stable complexity (mean 3.97 depth)
- **Medieval Latin**: Increased complexity during transition (mean 8.73 depth)
- **Spanish**: Return to manageable complexity (mean 4.52 depth)
- **Note**: Exploratory patterns only - requires future confirmation

## Methodology

### Corpus
- **7 Classical Latin texts**: Caesar, Cicero, Livy, Sallust
- **5 Medieval Latin texts**: Gregory of Tours, Bede, Isidore, Peregrinatio
- **4 Early Spanish texts**: Auto de los Reyes Magos, El Cid, Berceo, Fuero de Peñafiel

### Analysis Tools
- **Stanza NLP library** for Latin ('la') and Spanish ('es') linguistic annotation
- **Custom Python analysis** for complexity feature tracking
- **Non-parametric statistics** (Kruskal-Wallis, Mann-Whitney, Fisher's exact tests)

### Complexity Metrics
- Morphological complexity (case systems, verb morphology)
- Syntactic complexity (word order, dependency structures)  
- Functional elements (articles, prepositions, auxiliary constructions)

## Technical Implementation

### Requirements
```bash
pip install stanza pandas numpy matplotlib seaborn scipy requests beautifulsoup4
python -c "import stanza; stanza.download('la'); stanza.download('es')"
```

### Usage
```bash
# Download historical texts
python corpus_downloader.py

# Run complete analysis
python "example 1.py"
```

## Project Structure
```
linguistics/
├── corpus/
│   ├── classical_latin/     # Caesar, Cicero, Livy, Sallust
│   ├── medieval_latin/      # Gregory of Tours, Bede, Isidore
│   └── early_spanish/       # Auto, Cid, Berceo, Fuero
├── corpus_downloader.py     # Text collection from web sources
├── example 1.py            # Main analysis pipeline
├── results.md              # Detailed computational results
└── research-status-doc.md  # Comprehensive research documentation
```

## Detailed Results

### Article Development Analysis (CORRECTED)
- **Classical Latin**: 0.000 ± 0.000 articles per 1000 words (95% CI: [0.000, 0.000])
- **Medieval Latin**: 0.000 ± 0.000 articles per 1000 words (95% CI: [0.000, 0.000])
- **Spanish**: 107.018 ± 22.970 articles per 1000 words (95% CI: [85.774, 122.359])

**Statistical Tests:**
- Kruskal-Wallis H = 14.619, p = 0.0007
- Maximal difference between Latin (no articles) and Spanish (robust article system)

### Analytical Construction Evolution
- **Total Synthetic**: 6,182 (Classical Latin only)
- **Total Analytical**: 22 (Spanish only)  
- **Fisher's Exact Test**: p = 0.0001

### Dependency Complexity
- **Classical Latin**: 3.97 ± 0.28 depth (95% CI: [3.76, 4.17])
- **Medieval Latin**: 8.73 ± 5.27 depth (95% CI: [4.80, 13.62])
- **Spanish**: 4.52 ± 1.07 depth (95% CI: [3.34, 5.59])

## Research Significance

This work provides **quantitative evidence** for theoretical frameworks about language change, specifically challenging the assumption that languages necessarily simplify over time. Instead, it supports the **complexity conservation hypothesis** - that grammatical complexity redistributes across different subsystems while maintaining overall cognitive processing demands.

### Publications Status
- Two statistically significant findings supporting complexity conservation
- Novel computational methodology for historical linguistics
- Important methodological limitations properly acknowledged
- Preliminary findings requiring replication with larger samples
- Ready for submission as exploratory research to computational/historical linguistics journals

## Limitations

- **Medieval Latin Processing**: Stanza model limitations with Medieval Latin texts
- **Small Sample Sizes**: Typical of historical linguistics but addressed with non-parametric tests
- **Genre Variations**: Some variation across time periods controlled through text selection

## Citation

This research contributes to historical linguistics by providing computational evidence for complexity conservation in language change, with applications to theoretical linguistics, language evolution, and NLP model development for historical languages.

---

*Research conducted using computational methods with Stanza NLP and statistical analysis in Python.*