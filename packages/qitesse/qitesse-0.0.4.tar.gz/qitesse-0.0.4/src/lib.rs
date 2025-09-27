use pyo3::prelude::*;
use pyo3::types::PyList;
use numpy::{IntoPyArray, PyArray1};
use num_complex::Complex32;
use rayon::ThreadPoolBuilder;

mod sim;
use sim::{Circuit, Gate, StateVector};

/// Python wrapper for the Gate enum
#[pyclass(name = "Gate")]
#[derive(Clone)]
pub struct PyGate {
    gate: Gate,
}

#[pymethods]
impl PyGate {
    #[staticmethod]
    pub fn x(target: usize) -> Self {
        PyGate {
            gate: Gate::X(target),
        }
    }

    #[staticmethod]
    pub fn h(target: usize) -> Self {
        PyGate {
            gate: Gate::H(target),
        }
    }

    #[staticmethod]
    pub fn rz(target: usize, theta: f32) -> Self {
        PyGate {
            gate: Gate::RZ(target, theta),
        }
    }

    #[staticmethod]
    pub fn crz(control: usize, target: usize, theta: f32) -> Self {
        PyGate {
            gate: Gate::CRZ(control, target, theta),
        }
    }

    #[staticmethod]
    pub fn cnot(control: usize, target: usize) -> Self {
        PyGate {
            gate: Gate::CNOT(control, target),
        }
    }
}

/// Python wrapper for the Circuit struct
#[pyclass(name = "Circuit")]
pub struct PyCircuit {
    circuit: Circuit,
}

#[pymethods]
impl PyCircuit {
    #[new]
    pub fn new(gates: &PyList) -> Self {
        let rust_gates: Vec<Gate> = gates
            .iter()
            .map(|item| item.extract::<PyRef<PyGate>>().unwrap().gate.clone())
            .collect();
        PyCircuit {
            circuit: Circuit::new(rust_gates),
        }
    }

    pub fn run(&self, py: Python, num_qubits: usize) -> Py<PyArray1<Complex32>> {
        let mut state_vector = StateVector::new(num_qubits);
        self.circuit.run(&mut state_vector);
        state_vector.amps.into_pyarray(py).to_owned()
    }
}

/// Set the number of threads for Rayon
#[pyfunction]
fn set_num_threads(num_threads: usize) -> PyResult<()> {
    if num_threads == 0 {
        return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Number of threads must be greater than 0",
        ));
    }
    ThreadPoolBuilder::new()
        .num_threads(num_threads)
        .build_global()
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!(
            "Failed to set number of threads: {}",
            e
        )))?;
    println!("Using {} threads", rayon::current_num_threads());
    Ok(())
}

#[pymodule]
fn qitesse(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PyGate>()?;
    m.add_class::<PyCircuit>()?;
    m.add_function(wrap_pyfunction!(set_num_threads, m)?)?;
    Ok(())
}