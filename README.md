# Urban-Grid-Analysis
This repository provides a set of scripts for analyzing user trajectory data, generating grids within the city, and identifying frequently used origin-destination pairs. 
The gridding.py module focuses on generating grids within the city boundaries based on different levels of accuracy. These grids are used to divide the city into smaller regions. The module calculates the grid parameters and applies them to the user trajectory data, resulting in gridded origin-destination pairs and associated groups. 
The common_ods_plots.py module performs statistical analysis on the gridded data. It generates plots to visualize the distribution of origin-destination pairs . 
The common_ods_paths.py module extracts and saves the common origin-destination paths that have more than two associated trajectories.
