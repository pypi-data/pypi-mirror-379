# Privacy Models (PAPILLON-Inspired)

This submodule implements a privacy-preserving LLM pipeline inspired by:

**PAPILLON: PrivAcy Preservation from Internet-based and Local Language Model Ensembles**
Antoine Bosselut, et al.
arXiv: [2410.17127](https://arxiv.org/abs/2410.17127)

We adapt the PAPILLON methodology:
- Local model filters user input to reduce privacy leakage (LEAK).
- Remote model generates responses while preserving output quality (QUAL).
- Training/evaluation logic measures the QUAL–LEAK tradeoff.

If you use this code in research, please cite the original paper:

```bibtex
@article{bosselut2024papillon,
  title={PAPILLON: PrivAcy Preservation from Internet-based and Local Language Model Ensembles},
  author={Bosselut, Antoine and others},
  journal={arXiv preprint arXiv:2410.17127},
  year={2024}
}
