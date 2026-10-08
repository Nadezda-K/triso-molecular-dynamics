# Radiation Damage in TRISO Fuel: Molecular Simulation and Data Analysis

Python analysis of irradiation-induced structural changes at the interface between the porous buffer and inner pyrocarbon (IPyC) coating of TRISO nuclear fuel. The project connects atomistic simulations with quantitative measures of material damage, using a system containing **4,609,421 atoms**.

The repository contains research notebooks, post-processing scripts, simulation outputs, and the accompanying paper. It demonstrates scientific computing and data analysis workflows for turning large atomic-coordinate datasets into interpretable spatial profiles, structural features, and publication figures.

## Research context

TRISO fuel particles use multiple coating layers to retain fission products. Changes at the buffer–IPyC interface can influence the integrity of these coatings during irradiation.

The study uses LAMMPS molecular dynamics simulations of successive collision cascades to investigate how radiation damage accumulates. The porous buffer is represented by randomly oriented graphitic spheres, while the IPyC region is approximated by a graphite grain. The simulation protocol combines cascade evolution with relaxation at controlled temperature and pressure.

Analysis focuses on:

- Defect concentrations and atomic coordination across the interface.
- Density changes, buffer densification, and graphite deformation.
- Bond-length and bond-angle distributions as measures of structural disorder.
- Structural similarity between interface-adjacent layers and the material interior.
- Accumulated radiation dose, expressed as displacements per atom (dpa).

## Main findings

The accompanying paper reports buffer densification, graphite expansion perpendicular to its sheets, contraction within the sheets, and sheet buckling associated with radiation-induced cross-linking. Defects and structural disorder increase with irradiation, with more pronounced degradation near the interface than deeper within the graphite region. These trends help interpret published experimental observations of the buffer–IPyC interface.

## Data analysis workflow

1. **Parse simulation outputs:** read atomic coordinates, identifiers, coordination numbers, potential energies, and simulation metadata into tabular datasets.
2. **Construct spatial features:** divide the simulation cell into layers and account for changing cell dimensions during irradiation.
3. **Aggregate damage metrics:** calculate atomic populations, coordination-based defect counts, density profiles, and dose-dependent trends.
4. **Analyze local geometry:** use SciPy KD-tree neighbor searches to extract bond lengths and angles, then summarize their distributions.
5. **Visualize and interpret:** produce spatial profiles, structural similarity maps, and comparisons across irradiation stages.

## Repository guide

| File or directory | Purpose |
| --- | --- |
| `code_defects_vs_z_srinking.py` | Defect aggregation using separate layer partitions for the buffer and graphite regions. |
| `code_defects_vs_z_srinking_2.py` | Defect aggregation using a fixed number of layers across the changing simulation cell. |
| `a_defects_npt.ipynb` | Initial defect-profile analysis and visualization. |
| `a_defects_npt_shrinking.ipynb` | Defect, density, and interface analysis accounting for cell deformation. |
| `a_defects_npt_shrinking_redoing_selected_figures.ipynb` | Revised selected figures and structural similarity visualizations. |
| `a_bonds_npt_shrinking_part_1_data.ipynb` | Extraction of local bond geometry using KD-tree neighbor searches. |
| `a_bonds_npt_shrinking_part_2.ipynb` | Bond-length statistics and plots. |
| `a_bonds_npt_shrinking_part_3_angles.ipynb` | Bond-angle calculations, statistics, and plots. |
| `a_dpa_npt.ipynb` | Recoil-spectrum analysis and accumulated radiation-dose calculations. |
| `a_traject_npt.ipynb` | Parsing and preparation of atomic trajectory data. |
| `simulations_parameters_1-623_npt_aniso*.dat` | Simulation metadata used for dose and recoil analysis. |
| `recspec.out` | Recoil-spectrum data. |

Outputs contain layer boundaries, atom counts, coordination-based defect counts, and counts based on a potential-energy threshold.

## Tools and skills

**Tools:** Python, NumPy, pandas, SciPy, Matplotlib, Jupyter, OVITO, LAMMPS.

**Methods:** molecular dynamics, radiation-damage analysis, spatial binning, nearest-neighbor searches, feature extraction, descriptive statistics, dose-response analysis, and scientific visualization.

## Publication

N. Korepanova, Z. M. Krajewska-Travar, and A. E. Sand. **Simulation of the buffer-IPyC interface cell from the TRISO nuclear fuel with LAMMPS.** *Nuclear Instruments and Methods in Physics Research Section B*, **570** (2026), 165916.

[Read the publication](https://doi.org/10.1016/j.nimb.2025.165916) · [Research data](https://doi.org/10.5281/zenodo.14930110)

```bibtex
@article{Korepanova2026TRISO,
  title = {Simulation of the buffer-IPyC interface cell from the TRISO nuclear fuel with LAMMPS},
  author = {Korepanova, N. and Krajewska-Travar, Z. M. and Sand, A. E.},
  journal = {Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms},
  volume = {570},
  pages = {165916},
  year = {2026},
  doi = {10.1016/j.nimb.2025.165916}
}
```

## License

No code license is currently included in this repository. The accompanying article is published under CC BY 4.0; that license does not automatically establish the licensing terms for the repository's code or datasets.
