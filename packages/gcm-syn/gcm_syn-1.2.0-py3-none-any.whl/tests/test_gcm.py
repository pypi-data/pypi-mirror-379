import unittest
import numpy as np
from scipy.stats import pearsonr
from gcm import GCM


class TestGCM(unittest.TestCase):
    """
    Unit tests for the GCM (Generative Correlation Manifolds) class.
    
    Tests focus on:
    1. Correlation preservation in generated data
    2. Mean and standard deviation preservation when preserve_stats=True
    3. Standardized output (mean=0, std=1) when preserve_stats=False
    4. Basic functionality and error handling
    """
    
    def setUp(self):
        """Set up test data for use in test methods."""
        np.random.seed(42)  # For reproducible tests
        
        # Create test data with known correlation structure
        n_samples = 1000
        n_features = 4
        
        # Generate correlated data using a simple linear transformation
        base_data = np.random.normal(0, 1, (n_samples, n_features))
        
        # Create specific correlation structure
        self.test_data = np.copy(base_data)
        self.test_data[:, 1] = 0.8 * base_data[:, 0] + 0.6 * base_data[:, 1]  # Strong correlation with feature 0
        self.test_data[:, 2] = 0.5 * base_data[:, 0] + 0.866 * base_data[:, 2]  # Moderate correlation with feature 0
        self.test_data[:, 3] = base_data[:, 3]  # Independent
        
        # Scale and shift the data to have specific means and stds
        self.test_data = self.test_data * np.array([2, 3, 1.5, 0.8]) + np.array([10, -5, 0, 100])
        
        # Store expected statistics
        self.expected_mean = np.mean(self.test_data, axis=0)
        self.expected_std = np.std(self.test_data, axis=0, ddof=1)
        self.expected_corr = np.corrcoef(self.test_data, rowvar=False)
        
    def test_fit_basic_functionality(self):
        """Test basic fit functionality."""
        gcm = GCM()
        gcm.fit(self.test_data)
        
        self.assertTrue(gcm.is_fitted_)
        self.assertIsNotNone(gcm.cholesky_)
        self.assertEqual(gcm.cholesky_.shape, (self.test_data.shape[1], self.test_data.shape[1]))
        
    def test_fit_with_1d_data(self):
        """Test fit with 1D input data."""
        gcm = GCM()
        data_1d = np.random.normal(0, 1, 100)
        gcm.fit(data_1d)
        
        self.assertTrue(gcm.is_fitted_)
        self.assertEqual(gcm.cholesky_.shape, (1, 1))
        
    def test_fit_from_correlation_matrix(self):
        """Test fit_from_correlation method."""
        gcm = GCM()
        
        # Create a simple correlation matrix
        corr_matrix = np.array([[1.0, 0.5], [0.5, 1.0]])
        gcm.fit_from_correlation(corr_matrix)
        
        self.assertTrue(gcm.is_fitted_)
        self.assertEqual(gcm.cholesky_.shape, (2, 2))
        
    def test_fit_from_correlation_invalid_input(self):
        """Test fit_from_correlation with invalid input."""
        gcm = GCM()
        
        # Test with non-square matrix
        with self.assertRaises(ValueError):
            gcm.fit_from_correlation(np.array([[1.0, 0.5, 0.3], [0.5, 1.0]]))
            
    def test_sample_without_fit(self):
        """Test that sampling without fitting raises an error."""
        gcm = GCM()
        
        with self.assertRaises(RuntimeError):
            gcm.sample(100)
            
    def test_correlation_preservation(self):
        """Test that correlations are approximately preserved in generated data."""
        gcm = GCM(preserve_stats=False)  # Focus on correlations, not means/stds
        gcm.fit(self.test_data)
        
        # Generate synthetic data
        n_synthetic = 10000  # Large sample for better correlation estimation
        synthetic_data = gcm.sample(n_synthetic)
        
        # Compute correlation matrix of synthetic data
        synthetic_corr = np.corrcoef(synthetic_data, rowvar=False)
        
        # Check that correlations are preserved (within tolerance)
        tolerance = 0.05  # Allow 5% deviation
        
        for i in range(self.expected_corr.shape[0]):
            for j in range(self.expected_corr.shape[1]):
                expected = self.expected_corr[i, j]
                actual = synthetic_corr[i, j]
                
                with self.subTest(i=i, j=j):
                    self.assertAlmostEqual(
                        actual, expected, delta=tolerance,
                        msg=f"Correlation [{i},{j}] not preserved: expected {expected:.3f}, got {actual:.3f}"
                    )
                    
    def test_mean_std_preservation_when_true(self):
        """Test that means and stds are preserved when preserve_stats=True."""
        gcm = GCM(preserve_stats=True)
        gcm.fit(self.test_data)
        
        # Generate synthetic data
        n_synthetic = 5000
        synthetic_data = gcm.sample(n_synthetic)
        
        # Compute means and stds of synthetic data
        synthetic_mean = np.mean(synthetic_data, axis=0)
        synthetic_std = np.std(synthetic_data, axis=0, ddof=1)
        
        # Check means are preserved (within tolerance)
        mean_tolerance = 0.1  # Allow small deviation due to sampling
        for i in range(len(self.expected_mean)):
            with self.subTest(feature=i, stat='mean'):
                self.assertAlmostEqual(
                    synthetic_mean[i], self.expected_mean[i], delta=mean_tolerance,
                    msg=f"Mean for feature {i} not preserved: expected {self.expected_mean[i]:.3f}, got {synthetic_mean[i]:.3f}"
                )
                
        # Check stds are preserved (within tolerance)
        std_tolerance = 0.2  # Allow larger tolerance for std due to sampling variance
        for i in range(len(self.expected_std)):
            with self.subTest(feature=i, stat='std'):
                self.assertAlmostEqual(
                    synthetic_std[i], self.expected_std[i], delta=std_tolerance,
                    msg=f"Std for feature {i} not preserved: expected {self.expected_std[i]:.3f}, got {synthetic_std[i]:.3f}"
                )
                
    def test_standardized_output_when_false(self):
        """Test that output has mean≈0 and std≈1 when preserve_stats=False."""
        gcm = GCM(preserve_stats=False)
        gcm.fit(self.test_data)
        
        # Generate synthetic data
        n_synthetic = 5000
        synthetic_data = gcm.sample(n_synthetic)
        
        # Compute means and stds of synthetic data
        synthetic_mean = np.mean(synthetic_data, axis=0)
        synthetic_std = np.std(synthetic_data, axis=0, ddof=1)
        
        # Check means are close to 0
        mean_tolerance = 0.1
        for i in range(len(synthetic_mean)):
            with self.subTest(feature=i, stat='mean'):
                self.assertAlmostEqual(
                    synthetic_mean[i], 0.0, delta=mean_tolerance,
                    msg=f"Mean for feature {i} should be ~0: got {synthetic_mean[i]:.3f}"
                )
                
        # Check stds are close to 1
        std_tolerance = 0.1
        for i in range(len(synthetic_std)):
            with self.subTest(feature=i, stat='std'):
                self.assertAlmostEqual(
                    synthetic_std[i], 1.0, delta=std_tolerance,
                    msg=f"Std for feature {i} should be ~1: got {synthetic_std[i]:.3f}"
                )
                
    def test_sample_size_consistency(self):
        """Test that the correct number of samples is generated."""
        gcm = GCM()
        gcm.fit(self.test_data)
        
        for n_samples in [10, 100, 1000]:
            with self.subTest(n_samples=n_samples):
                synthetic_data = gcm.sample(n_samples)
                self.assertEqual(synthetic_data.shape[0], n_samples)
                self.assertEqual(synthetic_data.shape[1], self.test_data.shape[1])
                
    def test_different_random_seeds(self):
        """Test that different random seeds produce different results."""
        gcm = GCM()
        gcm.fit(self.test_data)
        
        np.random.seed(1)
        sample1 = gcm.sample(100)
        
        np.random.seed(2)
        sample2 = gcm.sample(100)
        
        # Samples should be different (very unlikely to be identical by chance)
        self.assertFalse(np.array_equal(sample1, sample2))
        
    def test_cholesky_decomposition_properties(self):
        """Test that the Cholesky decomposition has expected properties."""
        gcm = GCM()
        gcm.fit(self.test_data)
        
        L = gcm.cholesky_
        
        # L should be lower triangular
        self.assertTrue(np.allclose(L, np.tril(L)))
        
        # L @ L.T should reconstruct the original correlation matrix
        reconstructed = L @ L.T
        expected_corr = np.corrcoef(self.test_data, rowvar=False)
        
        self.assertTrue(np.allclose(reconstructed, expected_corr, atol=1e-10))
        
    def test_edge_case_perfect_correlation(self):
        """Test behavior with perfectly correlated data."""
        # Create perfectly correlated data
        n_samples = 100
        base = np.random.normal(0, 1, n_samples)
        perfect_corr_data = np.column_stack([base, 2 * base, -0.5 * base])
        
        gcm = GCM()
        
        # This might raise an error due to singular matrix
        # We test that it's handled gracefully
        try:
            gcm.fit(perfect_corr_data)
            synthetic = gcm.sample(50)
            
            # If it doesn't raise an error, check that correlations are preserved
            synthetic_corr = np.corrcoef(synthetic, rowvar=False)
            expected_corr = np.corrcoef(perfect_corr_data, rowvar=False)
            
            # Replace NaN with 0 for comparison (can happen with constant features)
            synthetic_corr = np.nan_to_num(synthetic_corr)
            expected_corr = np.nan_to_num(expected_corr)
            
            self.assertTrue(np.allclose(synthetic_corr, expected_corr, atol=0.1))
            
        except (np.linalg.LinAlgError, RuntimeError):
            # It's acceptable for the method to fail with singular matrices
            pass
            
    def test_single_feature_case(self):
        """Test behavior with single feature data."""
        single_feature_data = np.random.normal(5, 2, 100).reshape(-1, 1)
        
        gcm = GCM(preserve_stats=True)
        gcm.fit(single_feature_data)
        
        synthetic = gcm.sample(500)
        
        # Check shape
        self.assertEqual(synthetic.shape, (500, 1))
        
        # Check mean and std are approximately preserved
        original_mean = np.mean(single_feature_data)
        original_std = np.std(single_feature_data, ddof=1)
        
        synthetic_mean = np.mean(synthetic)
        synthetic_std = np.std(synthetic, ddof=1)
        
        self.assertAlmostEqual(synthetic_mean, original_mean, delta=0.2)
        self.assertAlmostEqual(synthetic_std, original_std, delta=0.3)
        
    def test_statistical_significance_of_correlations(self):
        """Test that preserved correlations are statistically significant."""
        gcm = GCM(preserve_stats=False)
        gcm.fit(self.test_data)
        
        synthetic_data = gcm.sample(2000)
        
        # Test specific correlation pairs that should be preserved
        for i in range(self.test_data.shape[1]):
            for j in range(i + 1, self.test_data.shape[1]):
                # Calculate correlation and p-value
                corr_coeff, p_value = pearsonr(synthetic_data[:, i], synthetic_data[:, j])
                expected_corr = self.expected_corr[i, j]
                
                with self.subTest(i=i, j=j):
                    # If original correlation was significant, synthetic should be too
                    if abs(expected_corr) > 0.3:  # Only test substantial correlations
                        self.assertLess(p_value, 0.05, 
                                      f"Correlation [{i},{j}] should be significant")
                        self.assertAlmostEqual(corr_coeff, expected_corr, delta=0.1,
                                             msg=f"Correlation coefficient not preserved")


class TestGCMIntegration(unittest.TestCase):
    """
    Integration tests for GCM that test the complete workflow.
    """
    
    def test_full_workflow_preserve_stats_true(self):
        """Test complete workflow with preserve_stats=True."""
        # Generate test data
        np.random.seed(123)
        original_data = np.random.multivariate_normal(
            mean=[10, -5, 2], 
            cov=[[4, 1, 0.5], [1, 9, -1], [0.5, -1, 1]], 
            size=1000
        )
        
        # Fit and generate
        gcm = GCM(preserve_stats=True)
        gcm.fit(original_data)
        synthetic_data = gcm.sample(2000)
        
        # Verify shape
        self.assertEqual(synthetic_data.shape[1], original_data.shape[1])
        
        # Verify statistics preservation
        orig_mean = np.mean(original_data, axis=0)
        orig_std = np.std(original_data, axis=0, ddof=1)
        synt_mean = np.mean(synthetic_data, axis=0)
        synt_std = np.std(synthetic_data, axis=0, ddof=1)
        
        np.testing.assert_allclose(synt_mean, orig_mean, atol=0.2)
        np.testing.assert_allclose(synt_std, orig_std, atol=0.3)
        
        # Verify correlation preservation
        orig_corr = np.corrcoef(original_data, rowvar=False)
        synt_corr = np.corrcoef(synthetic_data, rowvar=False)
        
        np.testing.assert_allclose(synt_corr, orig_corr, atol=0.1)
        
    def test_full_workflow_preserve_stats_false(self):
        """Test complete workflow with preserve_stats=False."""
        # Generate test data
        np.random.seed(456)
        original_data = np.random.multivariate_normal(
            mean=[100, -50, 20], 
            cov=[[16, 2, 1], [2, 25, -3], [1, -3, 4]], 
            size=800
        )
        
        # Fit and generate
        gcm = GCM(preserve_stats=False)
        gcm.fit(original_data)
        synthetic_data = gcm.sample(1500)
        
        # Verify standardized output
        synt_mean = np.mean(synthetic_data, axis=0)
        synt_std = np.std(synthetic_data, axis=0, ddof=1)
        
        np.testing.assert_allclose(synt_mean, np.zeros(3), atol=0.1)
        np.testing.assert_allclose(synt_std, np.ones(3), atol=0.1)
        
        # Verify correlation preservation
        orig_corr = np.corrcoef(original_data, rowvar=False)
        synt_corr = np.corrcoef(synthetic_data, rowvar=False)
        
        np.testing.assert_allclose(synt_corr, orig_corr, atol=0.1)


if __name__ == '__main__':
    unittest.main()
