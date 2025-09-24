# Generative Correlation Manifolds (GCM)

This Python package provides an implementation of the Generative Correlation Manifolds (GCM) method for generating synthetic data. The primary purpose of GCM is to generate data that either mimics the correlation structure of an existing dataset or adheres to a predefined correlation matrix. As described in the accompanying whitepaper, GCM is a computationally efficient method that is mathematically guaranteed to preserve the entire Pearson correlation structure of a z-normalized source dataset.

For a detailed description of the method and its mathematical foundations, please refer to the [whitepaper](whitepaper.pdf).

This makes it an ideal tool for a variety of tasks, including:

* Privacy-preserving data sharing
* Robust model augmentation
* High-fidelity simulation
* Algorithmic fairness and auditing

## Installation

To install the package though pip, use:

```bash
pip install gcm-syn
```

## Usage

The `GCM` class can be used in two main ways:

1. **Mimicking an Existing Dataset**: If you have a dataset and you want to generate more data with the same correlation structure.
2. **Creating a Dataset with a Specific Correlation Structure**: If you want to generate a dataset that has a correlation matrix you define.

### Parameters

The `GCM` class constructor accepts the following parameter:

* `preserve_stats` (bool, default=True): Whether to preserve the mean and standard deviation of the original data in the generated samples. When `True`, the synthetic data will have the same mean and standard deviation as the source data for each feature. When `False`, the generated data will be standardized (mean=0, std=1).

### Example 1: Mimicking an Existing Dataset

```python
import numpy as np
from gcm import GCM

# Assume `source_data` is a pre-existing dataset loaded into a numpy array
# For demonstration, we'll create a sample one:
mean = [0, 0, 0]
cov = [[1.0, 0.8, 0.3],
       [0.8, 1.0, 0.6],
       [0.3, 0.6, 1.0]]
source_data = np.random.multivariate_normal(mean, cov, 1000)

# 1. Initialize the GCM model (preserve_stats=True by default)
gcm = GCM()
gcm.fit(source_data)

# 2. Generate synthetic samples
synthetic_data = gcm.sample(num_samples=500)

# 3. Verify that the correlation structure is preserved
print("Source Correlation Matrix:")
print(np.corrcoef(source_data, rowvar=False))
print("\nSynthetic Correlation Matrix:")
print(np.corrcoef(synthetic_data, rowvar=False))

# 4. Verify that mean and standard deviation are preserved
print("\nSource Mean and Std:")
print(f"Mean: {np.mean(source_data, axis=0)}")
print(f"Std: {np.std(source_data, axis=0, ddof=1)}")
print("\nSynthetic Mean and Std:")
print(f"Mean: {np.mean(synthetic_data, axis=0)}")
print(f"Std: {np.std(synthetic_data, axis=0, ddof=1)}")
```

### Example 2: Creating a Dataset with a Specific Correlation Structure

To generate data with a specific correlation structure, you can now directly fit the GCM model with your target correlation matrix.

```python
import numpy as np
from gcm import GCM

# 1. Define your desired correlation structure
target_corr = np.array([[1.0, 0.8, 0.3],
                        [0.8, 1.0, 0.6],
                        [0.3, 0.6, 1.0]])

# 2. Initialize the GCM model and fit it to the correlation matrix.
gcm = GCM()
gcm.fit_from_correlation(target_corr)

# 3. Generate synthetic samples with the target correlation structure
synthetic_data = gcm.sample(num_samples=500)

# 4. Verify that the correlation structure matches the target
print("Target Correlation Matrix:")
print(target_corr)
print("\nSynthetic Correlation Matrix:")
print(np.corrcoef(synthetic_data, rowvar=False))
```

### Example 3: Generating Standardized Data

If you want to generate data with standardized values (mean=0, std=1) while preserving correlation structure:

```python
import numpy as np
from gcm import GCM

# Create some source data
mean = [10, 20, 30]
cov = [[4.0, 3.2, 1.2],
       [3.2, 9.0, 5.4],
       [1.2, 5.4, 16.0]]
source_data = np.random.multivariate_normal(mean, cov, 1000)

# Initialize GCM with preserve_stats=False for standardized output
gcm = GCM(preserve_stats=False)
gcm.fit(source_data)

# Generate standardized synthetic samples
synthetic_data = gcm.sample(num_samples=500)

print("Synthetic data statistics (should be ~0 mean, ~1 std):")
print(f"Mean: {np.mean(synthetic_data, axis=0)}")
print(f"Std: {np.std(synthetic_data, axis=0, ddof=1)}")
print("\nCorrelation structure is still preserved:")
print(np.corrcoef(synthetic_data, rowvar=False))
```
