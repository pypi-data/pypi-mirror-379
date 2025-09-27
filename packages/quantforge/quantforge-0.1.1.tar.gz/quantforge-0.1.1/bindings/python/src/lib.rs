//! Python bindings for QuantForge - Arrow-native implementation
//!
//! This module provides Python bindings for the QuantForge Arrow-native core library.

use pyo3::prelude::*;

mod arrow_common;
mod error;
mod market_utils;
mod models;
mod utils;

use models::*;

/// Main Python module definition
#[pymodule]
fn quantforge(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // Version information (automatically from Cargo.toml)
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;

    // ========================================================================
    // Black-Scholes Module
    // ========================================================================
    let black_scholes_module = PyModule::new(m.py(), "black_scholes")?;

    // Scalar functions
    black_scholes_module.add_function(wrap_pyfunction!(call_price, &black_scholes_module)?)?;
    black_scholes_module.add_function(wrap_pyfunction!(put_price, &black_scholes_module)?)?;
    black_scholes_module.add_function(wrap_pyfunction!(greeks, &black_scholes_module)?)?;
    black_scholes_module
        .add_function(wrap_pyfunction!(implied_volatility, &black_scholes_module)?)?;

    // Batch functions
    black_scholes_module
        .add_function(wrap_pyfunction!(call_price_batch, &black_scholes_module)?)?;
    black_scholes_module.add_function(wrap_pyfunction!(put_price_batch, &black_scholes_module)?)?;
    black_scholes_module.add_function(wrap_pyfunction!(greeks_batch, &black_scholes_module)?)?;
    black_scholes_module.add_function(wrap_pyfunction!(
        implied_volatility_batch,
        &black_scholes_module
    )?)?;

    // Fast batch functions (no validation for performance)
    black_scholes_module.add_function(wrap_pyfunction!(
        call_price_batch_no_validation,
        &black_scholes_module
    )?)?;
    black_scholes_module.add_function(wrap_pyfunction!(
        put_price_batch_no_validation,
        &black_scholes_module
    )?)?;

    m.add_submodule(&black_scholes_module)?;

    // Ensure the module is available at the package level
    let sys_modules = m.py().import("sys")?.getattr("modules")?;
    sys_modules.set_item("quantforge.black_scholes", &black_scholes_module)?;

    // ========================================================================
    // Black76 Module (Futures)
    // ========================================================================
    let black76_module = PyModule::new(m.py(), "black76")?;

    // Scalar functions
    black76_module.add_function(wrap_pyfunction!(black76_call_price, &black76_module)?)?;
    black76_module.add_function(wrap_pyfunction!(black76_put_price, &black76_module)?)?;
    black76_module.add_function(wrap_pyfunction!(black76_greeks, &black76_module)?)?;
    black76_module.add_function(wrap_pyfunction!(
        black76_implied_volatility,
        &black76_module
    )?)?;

    // Batch functions
    black76_module.add_function(wrap_pyfunction!(black76_call_price_batch, &black76_module)?)?;
    black76_module.add_function(wrap_pyfunction!(black76_put_price_batch, &black76_module)?)?;
    black76_module.add_function(wrap_pyfunction!(black76_greeks_batch, &black76_module)?)?;
    black76_module.add_function(wrap_pyfunction!(
        black76_implied_volatility_batch,
        &black76_module
    )?)?;

    m.add_submodule(&black76_module)?;
    sys_modules.set_item("quantforge.black76", &black76_module)?;

    // ========================================================================
    // Merton Module (Dividends)
    // ========================================================================
    let merton_module = PyModule::new(m.py(), "merton")?;

    // Scalar functions
    merton_module.add_function(wrap_pyfunction!(merton_call_price, &merton_module)?)?;
    merton_module.add_function(wrap_pyfunction!(merton_put_price, &merton_module)?)?;
    merton_module.add_function(wrap_pyfunction!(merton_greeks, &merton_module)?)?;
    merton_module.add_function(wrap_pyfunction!(merton_implied_volatility, &merton_module)?)?;

    // Batch functions
    merton_module.add_function(wrap_pyfunction!(merton_call_price_batch, &merton_module)?)?;
    merton_module.add_function(wrap_pyfunction!(merton_put_price_batch, &merton_module)?)?;
    merton_module.add_function(wrap_pyfunction!(merton_greeks_batch, &merton_module)?)?;
    merton_module.add_function(wrap_pyfunction!(
        merton_implied_volatility_batch,
        &merton_module
    )?)?;

    m.add_submodule(&merton_module)?;
    sys_modules.set_item("quantforge.merton", &merton_module)?;

    // ========================================================================
    // American Options Module
    // ========================================================================
    let american_module = PyModule::new(m.py(), "american")?;

    // Add functions with both full names and aliases
    // Scalar functions
    american_module.add_function(wrap_pyfunction!(american_call_price, &american_module)?)?;
    american_module.add_function(wrap_pyfunction!(american_put_price, &american_module)?)?;
    american_module.add_function(wrap_pyfunction!(
        american_call_price_adaptive,
        &american_module
    )?)?;
    american_module.add_function(wrap_pyfunction!(
        american_put_price_adaptive,
        &american_module
    )?)?;
    american_module.add_function(wrap_pyfunction!(american_greeks, &american_module)?)?;
    american_module.add_function(wrap_pyfunction!(
        american_implied_volatility,
        &american_module
    )?)?;
    american_module.add_function(wrap_pyfunction!(american_binomial, &american_module)?)?;
    american_module.add_function(wrap_pyfunction!(
        american_exercise_boundary,
        &american_module
    )?)?;

    // Batch functions
    american_module.add_function(wrap_pyfunction!(
        american_call_price_batch,
        &american_module
    )?)?;
    american_module.add_function(wrap_pyfunction!(
        american_put_price_batch,
        &american_module
    )?)?;
    american_module.add_function(wrap_pyfunction!(american_greeks_batch, &american_module)?)?;
    american_module.add_function(wrap_pyfunction!(
        american_implied_volatility_batch,
        &american_module
    )?)?;
    american_module.add_function(wrap_pyfunction!(
        american_exercise_boundary_batch,
        &american_module
    )?)?;

    m.add_submodule(&american_module)?;
    sys_modules.set_item("quantforge.american", &american_module)?;

    // ========================================================================
    // Market Utils Module
    // ========================================================================
    market_utils::register_module(m)?;
    sys_modules.set_item("quantforge.market_utils", m.getattr("market_utils")?)?;

    // ========================================================================
    // Arrow Native Module (Zero-Copy FFI functions from unified models.rs)
    // ========================================================================
    let arrow_module = PyModule::new(m.py(), "arrow_native")?;
    register_arrow_functions(&arrow_module)?; // Functions from models.rs

    m.add_submodule(&arrow_module)?;
    sys_modules.set_item("quantforge.arrow_native", &arrow_module)?;

    Ok(())
}
