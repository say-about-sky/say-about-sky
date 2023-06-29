use pyo3::prelude::*;
use rand::Rng;
use std::cmp::Ordering;
use std::io;

#[pyfunction]
#[pyo3(name = "")]
fn guess_the_number() {
    
}

#[pymodule]
#[pyo3(name = "")]
fn guessing_game(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(guess_the_number, m)?)?;

    Ok(())
}