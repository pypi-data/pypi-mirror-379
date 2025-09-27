//! Apache Arrow Native Implementation
//!
//! True zero-copy operations using Arrow arrays directly in Rust.
//! This module provides high-performance option pricing calculations
//! that operate directly on Arrow arrays without any data copying.

use arrow::array::Float64Array;
use rayon::prelude::*;

// Use centralized configuration from constants
use crate::constants::{get_parallel_threshold, THETA_DENOMINATOR_FACTOR};

// Use existing math functions
use crate::math::calculate_d1_d2 as calculate_d1_d2_common;
use crate::math::distributions::{norm_cdf, norm_pdf};

// Use validation utilities
use crate::validation::validate_option_inputs;

/// Calculate call option prices using Arrow arrays (zero-copy)
///
/// # Arguments
/// * `spots` - Spot prices as Arrow Float64Array
/// * `strikes` - Strike prices as Arrow Float64Array  
/// * `times` - Time to maturity as Arrow Float64Array
/// * `rates` - Risk-free rates as Arrow Float64Array
/// * `sigmas` - Volatilities as Arrow Float64Array
///
/// # Returns
/// Arrow Float64Array containing call option prices
pub fn arrow_call_price(
    spots: &Float64Array,
    strikes: &Float64Array,
    times: &Float64Array,
    rates: &Float64Array,
    sigmas: &Float64Array,
) -> Float64Array {
    let len = spots.len();

    // Choose between parallel and sequential processing based on size
    let threshold = get_parallel_threshold();
    if len >= threshold {
        // Parallel processing for large arrays
        let results: Vec<f64> = (0..len)
            .into_par_iter()
            .map(|i| {
                let s = spots.value(i);
                let k = strikes.value(i);
                let t = times.value(i);
                let r = rates.value(i);
                let sigma = sigmas.value(i);

                if validate_option_inputs(s, k, t, sigma).is_err() {
                    f64::NAN
                } else {
                    let (d1, d2) = calculate_d1_d2_common(s, k, t, r, 0.0, sigma);
                    s * norm_cdf(d1) - k * (-r * t).exp() * norm_cdf(d2)
                }
            })
            .collect();

        Float64Array::from(results)
    } else {
        // Sequential processing for small arrays
        let mut results = Vec::with_capacity(len);

        for i in 0..len {
            let s = spots.value(i);
            let k = strikes.value(i);
            let t = times.value(i);
            let r = rates.value(i);
            let sigma = sigmas.value(i);

            let price = if validate_option_inputs(s, k, t, sigma).is_err() {
                f64::NAN
            } else {
                let (d1, d2) = calculate_d1_d2_common(s, k, t, r, 0.0, sigma);
                s * norm_cdf(d1) - k * (-r * t).exp() * norm_cdf(d2)
            };

            results.push(price);
        }

        Float64Array::from(results)
    }
}

/// Calculate put option prices using Arrow arrays (zero-copy)
///
/// # Arguments
/// * `spots` - Spot prices as Arrow Float64Array
/// * `strikes` - Strike prices as Arrow Float64Array
/// * `times` - Time to maturity as Arrow Float64Array
/// * `rates` - Risk-free rates as Arrow Float64Array
/// * `sigmas` - Volatilities as Arrow Float64Array
///
/// # Returns
/// Arrow Float64Array containing put option prices
pub fn arrow_put_price(
    spots: &Float64Array,
    strikes: &Float64Array,
    times: &Float64Array,
    rates: &Float64Array,
    sigmas: &Float64Array,
) -> Float64Array {
    let len = spots.len();

    // Choose between parallel and sequential processing based on size
    let threshold = get_parallel_threshold();
    if len >= threshold {
        // Parallel processing for large arrays
        let results: Vec<f64> = (0..len)
            .into_par_iter()
            .map(|i| {
                let s = spots.value(i);
                let k = strikes.value(i);
                let t = times.value(i);
                let r = rates.value(i);
                let sigma = sigmas.value(i);

                if validate_option_inputs(s, k, t, sigma).is_err() {
                    f64::NAN
                } else {
                    let (d1, d2) = calculate_d1_d2_common(s, k, t, r, 0.0, sigma);
                    k * (-r * t).exp() * norm_cdf(-d2) - s * norm_cdf(-d1)
                }
            })
            .collect();

        Float64Array::from(results)
    } else {
        // Sequential processing for small arrays
        let mut results = Vec::with_capacity(len);

        for i in 0..len {
            let s = spots.value(i);
            let k = strikes.value(i);
            let t = times.value(i);
            let r = rates.value(i);
            let sigma = sigmas.value(i);

            let price = if validate_option_inputs(s, k, t, sigma).is_err() {
                f64::NAN
            } else {
                let (d1, d2) = calculate_d1_d2_common(s, k, t, r, 0.0, sigma);
                k * (-r * t).exp() * norm_cdf(-d2) - s * norm_cdf(-d1)
            };

            results.push(price);
        }

        Float64Array::from(results)
    }
}

/// Calculate Greeks for options using Arrow arrays
///
/// Returns a tuple of (delta, gamma, vega, theta, rho) as Arrow arrays
pub fn arrow_greeks(
    spots: &Float64Array,
    strikes: &Float64Array,
    times: &Float64Array,
    rates: &Float64Array,
    sigmas: &Float64Array,
    is_call: bool,
) -> (
    Float64Array,
    Float64Array,
    Float64Array,
    Float64Array,
    Float64Array,
) {
    let len = spots.len();

    // Calculate all Greeks in parallel for large arrays
    let threshold = get_parallel_threshold();
    if len >= threshold {
        let greeks: Vec<(f64, f64, f64, f64, f64)> = (0..len)
            .into_par_iter()
            .map(|i| {
                let s = spots.value(i);
                let k = strikes.value(i);
                let t = times.value(i);
                let r = rates.value(i);
                let sigma = sigmas.value(i);

                if t <= 0.0 || sigma <= 0.0 || s <= 0.0 || k <= 0.0 {
                    (f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN)
                } else {
                    calculate_greeks_single(s, k, t, r, sigma, is_call)
                }
            })
            .collect();

        // Unzip into separate arrays (manual unzip for 5-tuple)
        let mut deltas = Vec::with_capacity(len);
        let mut gammas = Vec::with_capacity(len);
        let mut vegas = Vec::with_capacity(len);
        let mut thetas = Vec::with_capacity(len);
        let mut rhos = Vec::with_capacity(len);

        for (delta, gamma, vega, theta, rho) in greeks {
            deltas.push(delta);
            gammas.push(gamma);
            vegas.push(vega);
            thetas.push(theta);
            rhos.push(rho);
        }

        (
            Float64Array::from(deltas),
            Float64Array::from(gammas),
            Float64Array::from(vegas),
            Float64Array::from(thetas),
            Float64Array::from(rhos),
        )
    } else {
        // Sequential processing for small arrays
        let mut deltas = Vec::with_capacity(len);
        let mut gammas = Vec::with_capacity(len);
        let mut vegas = Vec::with_capacity(len);
        let mut thetas = Vec::with_capacity(len);
        let mut rhos = Vec::with_capacity(len);

        for i in 0..len {
            let s = spots.value(i);
            let k = strikes.value(i);
            let t = times.value(i);
            let r = rates.value(i);
            let sigma = sigmas.value(i);

            let (delta, gamma, vega, theta, rho) =
                if t <= 0.0 || sigma <= 0.0 || s <= 0.0 || k <= 0.0 {
                    (f64::NAN, f64::NAN, f64::NAN, f64::NAN, f64::NAN)
                } else {
                    calculate_greeks_single(s, k, t, r, sigma, is_call)
                };

            deltas.push(delta);
            gammas.push(gamma);
            vegas.push(vega);
            thetas.push(theta);
            rhos.push(rho);
        }

        (
            Float64Array::from(deltas),
            Float64Array::from(gammas),
            Float64Array::from(vegas),
            Float64Array::from(thetas),
            Float64Array::from(rhos),
        )
    }
}

/// Helper function to calculate Greeks for a single option
fn calculate_greeks_single(
    s: f64,
    k: f64,
    t: f64,
    r: f64,
    sigma: f64,
    is_call: bool,
) -> (f64, f64, f64, f64, f64) {
    let (d1, d2) = calculate_d1_d2_common(s, k, t, r, 0.0, sigma);
    let sqrt_t = t.sqrt();
    let exp_rt = (-r * t).exp();

    // Standard normal PDF
    let phi_d1 = norm_pdf(d1);
    // Note: phi_d2 is not used in current calculations

    // Delta
    let delta = if is_call {
        norm_cdf(d1)
    } else {
        norm_cdf(d1) - 1.0
    };

    // Gamma (same for call and put)
    let gamma = phi_d1 / (s * sigma * sqrt_t);

    // Vega (same for call and put)
    let vega = s * phi_d1 * sqrt_t;

    // Theta
    let theta = if is_call {
        -(s * phi_d1 * sigma) / (THETA_DENOMINATOR_FACTOR * sqrt_t) - r * k * exp_rt * norm_cdf(d2)
    } else {
        -(s * phi_d1 * sigma) / (THETA_DENOMINATOR_FACTOR * sqrt_t) + r * k * exp_rt * norm_cdf(-d2)
    };

    // Rho
    let rho = if is_call {
        k * t * exp_rt * norm_cdf(d2)
    } else {
        -k * t * exp_rt * norm_cdf(-d2)
    };

    (delta, gamma, vega, theta, rho)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::constants::ARROW_PRECISION_THRESHOLD;

    #[test]
    fn test_arrow_call_price_basic() {
        let spots = Float64Array::from(vec![100.0]);
        let strikes = Float64Array::from(vec![105.0]);
        let times = Float64Array::from(vec![1.0]);
        let rates = Float64Array::from(vec![0.05]);
        let sigmas = Float64Array::from(vec![0.2]);

        let result = arrow_call_price(&spots, &strikes, &times, &rates, &sigmas);

        // Expected value from Black-Scholes formula
        assert!((result.value(0) - 8.021352235143176).abs() < ARROW_PRECISION_THRESHOLD);
    }

    #[test]
    fn test_arrow_put_price_basic() {
        let spots = Float64Array::from(vec![100.0]);
        let strikes = Float64Array::from(vec![105.0]);
        let times = Float64Array::from(vec![1.0]);
        let rates = Float64Array::from(vec![0.05]);
        let sigmas = Float64Array::from(vec![0.2]);

        let result = arrow_put_price(&spots, &strikes, &times, &rates, &sigmas);

        // Expected value from Black-Scholes formula (verified against existing implementation)
        let actual = result.value(0);
        let expected = 7.9004418077181455;
        assert!(
            (actual - expected).abs() < ARROW_PRECISION_THRESHOLD,
            "Put price mismatch: expected {expected}, got {actual}"
        );
    }

    #[test]
    fn test_parallel_processing() {
        let size = 100_000;
        let spots = Float64Array::from(vec![100.0; size]);
        let strikes = Float64Array::from(vec![105.0; size]);
        let times = Float64Array::from(vec![1.0; size]);
        let rates = Float64Array::from(vec![0.05; size]);
        let sigmas = Float64Array::from(vec![0.2; size]);

        let result = arrow_call_price(&spots, &strikes, &times, &rates, &sigmas);

        assert_eq!(result.len(), size);
        // All results should be the same
        for i in 0..size {
            assert!((result.value(i) - 8.021352235143176).abs() < ARROW_PRECISION_THRESHOLD);
        }
    }
}
