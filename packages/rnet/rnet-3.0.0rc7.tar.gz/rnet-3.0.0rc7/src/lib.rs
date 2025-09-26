#![deny(unused)]
#![deny(unsafe_code)]
#![cfg_attr(test, deny(warnings))]
#![cfg_attr(not(test), warn(unused_crate_dependencies))]

#[cfg(feature = "mimalloc")]
use mimalloc as _;
#[cfg(feature = "jemalloc")]
use tikv_jemallocator as _;

#[macro_use]
mod macros;
mod buffer;
mod client;
mod emulation;
mod error;
mod extractor;
mod http;
mod http1;
mod http2;
mod proxy;
mod rt;
mod tls;

use pyo3::{prelude::*, pybacked::PyBackedStr, types::PyDict, wrap_pymodule};

use self::{
    client::{
        BlockingClient, Client, SocketAddr,
        body::multipart::{Multipart, Part},
        execute_request, execute_websocket_request,
        req::{Request, WebSocketRequest},
        resp::{
            BlockingResponse, BlockingWebSocket, History, Message, Response, Streamer, WebSocket,
        },
    },
    emulation::{Emulation, EmulationOS, EmulationOption},
    error::*,
    http::{
        Method, Version,
        cookie::{Cookie, Jar, SameSite},
        header::{HeaderMap, OrigHeaderMap},
        status::StatusCode,
    },
    http1::Http1Options,
    http2::{
        Http2Options, Priorities, Priority, PseudoId, PseudoOrder, SettingId, SettingsOrder,
        StreamDependency, StreamId,
    },
    proxy::Proxy,
    rt::Runtime,
    tls::{
        AlpnProtocol, AlpsProtocol, CertStore, CertificateCompressionAlgorithm, ExtensionType,
        Identity, KeyLog, TlsOptions, TlsVersion,
    },
};

#[cfg(all(feature = "jemalloc", not(feature = "mimalloc"),))]
#[global_allocator]
static GLOBAL: tikv_jemallocator::Jemalloc = tikv_jemallocator::Jemalloc;

#[cfg(all(feature = "mimalloc", not(feature = "jemalloc")))]
#[global_allocator]
static GLOBAL: mimalloc::MiMalloc = mimalloc::MiMalloc;

/// Make a GET request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn get(py: Python<'_>, url: PyBackedStr, kwds: Option<Request>) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::GET, url, kwds))
}

/// Make a POST request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn post(py: Python<'_>, url: PyBackedStr, kwds: Option<Request>) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::POST, url, kwds))
}

/// Make a PUT request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn put(py: Python<'_>, url: PyBackedStr, kwds: Option<Request>) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::PUT, url, kwds))
}

/// Make a PATCH request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn patch(
    py: Python<'_>,
    url: PyBackedStr,
    kwds: Option<Request>,
) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::PATCH, url, kwds))
}

/// Make a DELETE request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn delete(
    py: Python<'_>,
    url: PyBackedStr,
    kwds: Option<Request>,
) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::DELETE, url, kwds))
}

/// Make a HEAD request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn head(py: Python<'_>, url: PyBackedStr, kwds: Option<Request>) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::HEAD, url, kwds))
}

/// Make a OPTIONS request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn options(
    py: Python<'_>,
    url: PyBackedStr,
    kwds: Option<Request>,
) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::OPTIONS, url, kwds))
}

/// Make a TRACE request with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn trace(
    py: Python<'_>,
    url: PyBackedStr,
    kwds: Option<Request>,
) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, Method::TRACE, url, kwds))
}

/// Make a request with the given parameters.
#[pyfunction]
#[pyo3(signature = (method, url, **kwds))]
pub fn request(
    py: Python<'_>,
    method: Method,
    url: PyBackedStr,
    kwds: Option<Request>,
) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_request(None, method, url, kwds))
}

/// Make a WebSocket connection with the given parameters.
#[pyfunction]
#[pyo3(signature = (url, **kwds))]
pub fn websocket(
    py: Python<'_>,
    url: PyBackedStr,
    kwds: Option<WebSocketRequest>,
) -> PyResult<Bound<'_, PyAny>> {
    Runtime::future_into_py(py, execute_websocket_request(None, url, kwds))
}

#[pymodule(gil_used = false)]
fn rnet(py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    Python::initialize();

    m.add_class::<SocketAddr>()?;
    m.add_class::<Message>()?;
    m.add_class::<StatusCode>()?;
    m.add_class::<Part>()?;
    m.add_class::<Multipart>()?;
    m.add_class::<Client>()?;
    m.add_class::<Response>()?;
    m.add_class::<History>()?;
    m.add_class::<WebSocket>()?;
    m.add_class::<Streamer>()?;
    m.add_class::<Proxy>()?;
    m.add_class::<Method>()?;
    m.add_class::<Version>()?;

    m.add_function(wrap_pyfunction!(get, m)?)?;
    m.add_function(wrap_pyfunction!(post, m)?)?;
    m.add_function(wrap_pyfunction!(put, m)?)?;
    m.add_function(wrap_pyfunction!(patch, m)?)?;
    m.add_function(wrap_pyfunction!(delete, m)?)?;
    m.add_function(wrap_pyfunction!(head, m)?)?;
    m.add_function(wrap_pyfunction!(options, m)?)?;
    m.add_function(wrap_pyfunction!(trace, m)?)?;
    m.add_function(wrap_pyfunction!(request, m)?)?;
    m.add_function(wrap_pyfunction!(websocket, m)?)?;

    m.add_wrapped(wrap_pymodule!(http1_module))?;
    m.add_wrapped(wrap_pymodule!(http2_module))?;
    m.add_wrapped(wrap_pymodule!(tls_module))?;
    m.add_wrapped(wrap_pymodule!(header_module))?;
    m.add_wrapped(wrap_pymodule!(cookie_module))?;
    m.add_wrapped(wrap_pymodule!(emulation_module))?;
    m.add_wrapped(wrap_pymodule!(blocking_module))?;
    m.add_wrapped(wrap_pymodule!(exceptions_module))?;

    let sys = PyModule::import(py, "sys")?;
    let sys_modules: Bound<'_, PyDict> = sys.getattr("modules")?.downcast_into()?;
    sys_modules.set_item("rnet.http1", m.getattr("http1")?)?;
    sys_modules.set_item("rnet.http2", m.getattr("http2")?)?;
    sys_modules.set_item("rnet.tls", m.getattr("tls")?)?;
    sys_modules.set_item("rnet.header", m.getattr("header")?)?;
    sys_modules.set_item("rnet.cookie", m.getattr("cookie")?)?;
    sys_modules.set_item("rnet.emulation", m.getattr("emulation")?)?;
    sys_modules.set_item("rnet.blocking", m.getattr("blocking")?)?;
    sys_modules.set_item("rnet.exceptions", m.getattr("exceptions")?)?;
    Ok(())
}

#[pymodule(gil_used = false, name = "http1")]
fn http1_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Http1Options>()?;
    Ok(())
}

#[pymodule(gil_used = false, name = "http2")]
fn http2_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Http2Options>()?;
    m.add_class::<StreamId>()?;
    m.add_class::<StreamDependency>()?;
    m.add_class::<Priorities>()?;
    m.add_class::<Priority>()?;
    m.add_class::<PseudoId>()?;
    m.add_class::<PseudoOrder>()?;
    m.add_class::<SettingId>()?;
    m.add_class::<SettingsOrder>()?;
    Ok(())
}

#[pymodule(gil_used = false, name = "tls")]
fn tls_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<TlsVersion>()?;
    m.add_class::<Identity>()?;
    m.add_class::<CertStore>()?;
    m.add_class::<KeyLog>()?;
    m.add_class::<AlpnProtocol>()?;
    m.add_class::<AlpsProtocol>()?;
    m.add_class::<CertificateCompressionAlgorithm>()?;
    m.add_class::<ExtensionType>()?;
    m.add_class::<TlsOptions>()?;
    Ok(())
}

#[pymodule(gil_used = false, name = "header")]
fn header_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<HeaderMap>()?;
    m.add_class::<OrigHeaderMap>()?;
    Ok(())
}

#[pymodule(gil_used = false, name = "cookie")]
fn cookie_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Jar>()?;
    m.add_class::<Cookie>()?;
    m.add_class::<SameSite>()?;
    Ok(())
}

#[pymodule(gil_used = false, name = "emulation")]
fn emulation_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Emulation>()?;
    m.add_class::<EmulationOS>()?;
    m.add_class::<EmulationOption>()?;
    Ok(())
}

#[pymodule(gil_used = false, name = "blocking")]
fn blocking_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<BlockingClient>()?;
    m.add_class::<BlockingResponse>()?;
    m.add_class::<BlockingWebSocket>()?;
    Ok(())
}

#[pymodule(gil_used = false, name = "exceptions")]
fn exceptions_module(py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add("DNSResolverError", py.get_type::<DNSResolverError>())?;
    m.add("TlsError", py.get_type::<TlsError>())?;
    m.add("BodyError", py.get_type::<BodyError>())?;
    m.add("BuilderError", py.get_type::<BuilderError>())?;
    m.add("ConnectionError", py.get_type::<ConnectionError>())?;
    m.add(
        "ConnectionResetError",
        py.get_type::<ConnectionResetError>(),
    )?;
    m.add("DecodingError", py.get_type::<DecodingError>())?;
    m.add("RedirectError", py.get_type::<RedirectError>())?;
    m.add("TimeoutError", py.get_type::<TimeoutError>())?;
    m.add("StatusError", py.get_type::<StatusError>())?;
    m.add("RequestError", py.get_type::<RequestError>())?;
    m.add("UpgradeError", py.get_type::<UpgradeError>())?;
    m.add("WebSocketError", py.get_type::<WebSocketError>())?;
    m.add("URLParseError", py.get_type::<URLParseError>())?;
    m.add("RustPanic", py.get_type::<RustPanic>())?;
    Ok(())
}
