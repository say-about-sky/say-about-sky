use pyo3::prelude::*;
use rand::Rng;
use std::cmp::Ordering;
use std::io;
// pyfunction:

#[pymodule]
#[pyo3(name = "")]
fn guessing_game(_py: Python, m: &PyModule) -> PyResult<()> {
    // add_pyfunction:

    Ok(())
}