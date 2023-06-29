use pyo3::prelude::*;
use rand::Rng;
use std::cmp::Ordering;
use std::io;
// pyfunction:
#[pyfunction]
fn f(){
println!("ok")
}
#[pymodule]
#[pyo3(name = "yy")]
fn guessing_game(_py: Python, m: &PyModule) -> PyResult<()> {
    // add_pyfunction:

    m.add_function(wrap_pyfunction!(f,m)?)?;
Ok(())
}