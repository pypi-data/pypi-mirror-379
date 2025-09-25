# 🏷️ TagForge

<p align="center">
  <img src="docs/assets/banner.png" alt="TagForge Logo" width="600"/>
</p>

**Forge meaningful tags from raw content with AI.**

TagForge is an open-source tool that uses **LLMs + dspy** to automatically generate smart, context-aware tags for blog posts, articles, and other written content.
It helps writers, developers, and teams improve discoverability and organization with **semantic tagging** powered by AI.

## Installation

TagForge prefers to use a local LLM for preserving PII information.

### Macos

```bash
brew install ollama
brew services start ollama
ollama pull llama3.1:8b
```

## Privacy Preservation (PAPILLON-Inspired)

This project implements a privacy-preserving pipeline inspired by:

- **PAPILLON: PrivAcy Preservation from Internet-based and Local Language Model Ensembles**
  Antoine Bosselut, et al.
  arXiv: [2410.17127](https://arxiv.org/abs/2410.17127)

Our implementation adapts their core methodology (local filtering + remote API model + evaluation on QUAL/LEAK) within a DSPy framework.
