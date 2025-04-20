# Analysis of Lakhina Volume 1 - Botnet Detection Algorithm

In this project, you will find the implementation of the Lakhina Volume 1 algorithm for botnet detection. The algorithm is designed to analyze network traffic data and identify potential botnet activity.

## Overview

The Lakhina Volume 1 algorithm is a machine learning-based approach that uses statistical techniques to detect anomalies in network traffic. The algorithm is capable of identifying patterns in the data that may indicate the presence of a botnet. It works by analyzing the flow of data packets and identifying unusual patterns that deviate from normal behavior.

The code is designed to be modular and easy to understand, making it suitable for both beginners and experienced developers.

The project includes :

- a Jupyter notebook that demonstrates the algorithm's functionality ;
- a Python script that automates the execution of the notebook for multiple datasets ;
- a set of datasets that can be used to test the algorithm ;
- the output of the algorithm for each dataset ;
- a report that analyzes the results of the algorithm and provides insights into its performance.

For more information about the algorithm and its implementation, please read [our report](Rapport.pdf).

## Requirements

Before running the code, you need to install the 13 datasets [here](https://mega.nz/folder/vdRmBA6D#yMZXx74nnu8GjhdwSF54Sw). Totally, the datasets are about 80 GB in size.

Next, you need to put the 13 datasets in `CTU-13-Dataset/CTU-13-Dataset/` folder and rename them with a number from 1 to 13. For example, the first dataset should be named `1` and the second one should be named `2`. The datasets include pcap files containing network traffic data captured during botnet activity.

Please respect the order of the datasets:

- `CTU-13.Dataset-42` should be renamed to `1`
- `CTU-13.Dataset-43` should be renamed to `2`
- ...

## Installation

To run the code:

```bash
pip install papermill
python main.py
```

This will automatically run the lakhina.ipynb program for the 13 test datasets. The results will be displayed in the output folder.
