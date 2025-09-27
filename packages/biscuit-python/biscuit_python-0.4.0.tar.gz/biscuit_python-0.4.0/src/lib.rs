/*
 * SPDX-FileCopyrightText: 2022 Josh Wright, Clément Delafargue
 *
 * SPDX-License-Identifier: Apache-2.0
 */
// There seem to be false positives with pyo3
#![allow(clippy::borrow_deref_ref)]
#![allow(unexpected_cfgs)]
#![allow(clippy::useless_conversion)]
use ::biscuit_auth::builder::MapKey;
use ::biscuit_auth::datalog::ExternFunc;
use ::biscuit_auth::AuthorizerBuilder;
use ::biscuit_auth::RootKeyProvider;
use ::biscuit_auth::ThirdPartyBlock;
use ::biscuit_auth::ThirdPartyRequest;
use ::biscuit_auth::UnverifiedBiscuit;
use chrono::DateTime;
use chrono::Duration;
use chrono::TimeZone;
use chrono::Utc;
use std::collections::BTreeSet;
use std::collections::HashMap;
use std::ops::Deref;
use std::str::FromStr;
use std::sync::Arc;

use ::biscuit_auth::{
    builder, error, Authorizer, AuthorizerLimits, Biscuit, KeyPair, PrivateKey, PublicKey,
};

use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::*;

use pyo3::create_exception;

create_exception!(biscuit_auth, DataLogError, pyo3::exceptions::PyException);
create_exception!(
    biscuit_auth,
    AuthorizationError,
    pyo3::exceptions::PyException
);
create_exception!(
    biscuit_auth,
    BiscuitBuildError,
    pyo3::exceptions::PyException
);
create_exception!(
    biscuit_auth,
    BiscuitValidationError,
    pyo3::exceptions::PyException
);
create_exception!(
    biscuit_auth,
    BiscuitSerializationError,
    pyo3::exceptions::PyException
);
create_exception!(
    biscuit_auth,
    BiscuitBlockError,
    pyo3::exceptions::PyException
);

#[pyclass(eq, eq_int, name = "Algorithm")]
#[derive(PartialEq, Eq, Clone, Copy)]
pub enum PyAlgorithm {
    Ed25519,
    Secp256r1,
}

impl From<builder::Algorithm> for PyAlgorithm {
    fn from(value: builder::Algorithm) -> Self {
        match value {
            builder::Algorithm::Ed25519 => Self::Ed25519,
            builder::Algorithm::Secp256r1 => Self::Secp256r1,
        }
    }
}
impl From<PyAlgorithm> for builder::Algorithm {
    fn from(value: PyAlgorithm) -> Self {
        match value {
            PyAlgorithm::Ed25519 => Self::Ed25519,
            PyAlgorithm::Secp256r1 => Self::Secp256r1,
        }
    }
}

struct PyKeyProvider {
    py_value: PyObject,
}

impl RootKeyProvider for PyKeyProvider {
    fn choose(&self, kid: Option<u32>) -> Result<PublicKey, error::Format> {
        Python::with_gil(|py| {
            let bound = self.py_value.bind(py);
            if bound.is_callable() {
                let result = bound
                    .call1((kid,))
                    .map_err(|_| error::Format::UnknownPublicKey)?;
                let py_pk: PyPublicKey = result
                    .extract()
                    .map_err(|_| error::Format::UnknownPublicKey)?;
                Ok(py_pk.0)
            } else {
                let py_pk: PyPublicKey = bound
                    .extract()
                    .map_err(|_| error::Format::UnknownPublicKey)?;
                Ok(py_pk.0)
            }
        })
    }
}

/// Builder class allowing to create a biscuit from a datalog block
///
/// :param source: a datalog snippet
/// :type source: str, optional
/// :param parameters: values for the parameters in the datalog snippet
/// :type parameters: dict, optional
/// :param scope_parameters: public keys for the public key parameters in the datalog snippet
/// :type scope_parameters: dict, optional
#[pyclass(name = "BiscuitBuilder")]
pub struct PyBiscuitBuilder(Option<builder::BiscuitBuilder>);

#[pymethods]
impl PyBiscuitBuilder {
    /// Create a builder from a datalog snippet and optional parameter values
    ///
    /// :param source: a datalog snippet
    /// :type source: str, optional
    /// :param parameters: values for the parameters in the datalog snippet
    /// :type parameters: dict, optional
    /// :param scope_parameters: public keys for the public key parameters in the datalog snippet
    /// :type scope_parameters: dict, optional
    #[new]
    #[pyo3(signature = (source=None, parameters=None, scope_parameters=None))]
    fn new(
        source: Option<String>,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<PyBiscuitBuilder> {
        let mut builder = PyBiscuitBuilder(Some(builder::BiscuitBuilder::new()));
        if let Some(source) = source {
            builder.add_code(&source, parameters, scope_parameters)?;
        }
        Ok(builder)
    }

    /// Build a biscuit token, using the provided private key to sign the authority block
    ///
    /// :param root: a keypair that will be used to sign the authority block
    /// :type root: PrivateKey
    /// :return: a biscuit token
    /// :rtype: Biscuit
    pub fn build(&self, root: &PyPrivateKey) -> PyResult<PyBiscuit> {
        let keypair = KeyPair::from(&root.0);
        Ok(PyBiscuit(
            self.0
                .clone()
                .expect("builder already consumed")
                .build(&keypair)
                .map_err(|e| BiscuitBuildError::new_err(e.to_string()))?,
        ))
    }

    /// Add code to the builder, using the provided parameters.
    ///
    /// :param source: a datalog snippet
    /// :type source: str, optional
    /// :param parameters: values for the parameters in the datalog snippet
    /// :type parameters: dict, optional
    /// :param scope_parameters: public keys for the public key parameters in the datalog snippet
    /// :type scope_parameters: dict, optional
    #[pyo3(signature = (source, parameters=None, scope_parameters=None))]
    pub fn add_code(
        &mut self,
        source: &str,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<()> {
        let mut params = HashMap::new();

        if let Some(parameters) = parameters {
            for (k, v) in parameters {
                params.insert(k, v.to_term()?);
            }
        }

        let scope_params;

        if let Some(scope_parameters) = scope_parameters {
            scope_params = scope_parameters
                .iter()
                .map(|(k, v)| (k.to_string(), v.0))
                .collect();
        } else {
            scope_params = HashMap::new();
        }

        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .code_with_params(source, params, scope_params)
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single fact to the builder. A single fact can be built with
    /// the `Fact` class and its constructor
    ///
    /// :param fact: a datalog fact
    /// :type fact: Fact
    pub fn add_fact(&mut self, fact: &PyFact) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .fact(fact.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single rule to the builder. A single rule can be built with
    /// the `Rule` class and its constructor
    ///
    /// :param rule: a datalog rule
    /// :type rule: Rule
    pub fn add_rule(&mut self, rule: &PyRule) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .rule(rule.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single check to the builder. A single check can be built with
    /// the `Check` class and its constructor
    ///
    /// :param check: a datalog check
    /// :type check: Check
    pub fn add_check(&mut self, check: &PyCheck) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .check(check.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Merge a `BlockBuilder` in this `BiscuitBuilder`. The `BlockBuilder` parameter will not be modified
    ///
    /// :param builder: a datalog BlockBuilder
    /// :type builder: BlockBuilder
    pub fn merge(&mut self, builder: &PyBlockBuilder) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .merge(builder.0.clone().expect("builder already consumed")),
        );

        Ok(())
    }

    /// Set the root key identifier for this `BiscuitBuilder`
    ///
    /// :param root_key_id: the root key identifier
    /// :type root_key_id: int
    pub fn set_root_key_id(&mut self, root_key_id: u32) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .root_key_id(root_key_id),
        );
        Ok(())
    }

    fn __repr__(&self) -> String {
        match self.0 {
            Some(ref b) => b.to_string(),
            None => "_ BiscuitBuilder already consumed_".to_string(),
        }
    }
}

/// Representation of a biscuit token that has been parsed and cryptographically verified.
#[pyclass(name = "Biscuit")]
pub struct PyBiscuit(Biscuit);

#[pymethods]
impl PyBiscuit {
    /// Creates a BiscuitBuilder
    ///
    /// :return: an empty BiscuitBuilder
    /// :rtype: BiscuitBuilder
    #[staticmethod]
    pub fn builder() -> PyResult<PyBiscuitBuilder> {
        PyBiscuitBuilder::new(None, None, None)
    }

    /// Deserializes a token from raw data
    ///
    /// This will check the signature using the provided root key (or function)
    ///
    /// :param data: raw biscuit bytes
    /// :type data: bytes
    /// :param root: either a public key or a function taking an integer (or `None`) and returning an public key
    /// :type root: function,PublicKey
    /// :return: the parsed and verified biscuit
    /// :rtype: Biscuit
    #[classmethod]
    pub fn from_bytes(_: &Bound<PyType>, data: &[u8], root: PyObject) -> PyResult<PyBiscuit> {
        match Biscuit::from(data, PyKeyProvider { py_value: root }) {
            Ok(biscuit) => Ok(PyBiscuit(biscuit)),
            Err(error) => Err(BiscuitValidationError::new_err(error.to_string())),
        }
    }

    /// Deserializes a token from URL safe base 64 data
    ///
    /// This will check the signature using the provided root key (or function)
    ///
    /// :param data: a (url-safe) base64-encoded string
    /// :type data: str
    /// :param root: either a public key or a function taking an integer (or `None`) and returning an public key
    /// :type root: function,PublicKey
    /// :return: the parsed and verified biscuit
    /// :rtype: Biscuit
    #[classmethod]
    pub fn from_base64(_: &Bound<PyType>, data: &str, root: PyObject) -> PyResult<PyBiscuit> {
        match Biscuit::from_base64(data, PyKeyProvider { py_value: root }) {
            Ok(biscuit) => Ok(PyBiscuit(biscuit)),
            Err(error) => Err(BiscuitValidationError::new_err(error.to_string())),
        }
    }

    /// Serializes to raw bytes
    ///
    /// :return: the serialized biscuit
    /// :rtype: list
    pub fn to_bytes(&self) -> PyResult<Vec<u8>> {
        match self.0.to_vec() {
            Ok(vec) => Ok(vec),
            Err(error) => Err(BiscuitSerializationError::new_err(error.to_string())),
        }
    }

    /// Serializes to URL safe base 64 data
    ///
    /// :return: the serialized biscuit
    /// :rtype: str
    pub fn to_base64(&self) -> String {
        self.0.to_base64().unwrap()
    }

    /// Returns the number of blocks in the token
    ///
    /// :return: the number of blocks
    /// :rtype: int
    pub fn block_count(&self) -> usize {
        self.0.block_count()
    }

    /// Prints a block's content as Datalog code
    ///
    /// :param index: the block index
    /// :type index: int
    /// :return: the code for the corresponding block
    /// :rtype: str
    pub fn block_source(&self, index: usize) -> PyResult<String> {
        self.0
            .print_block_source(index)
            .map_err(|e| BiscuitBlockError::new_err(e.to_string()))
    }

    /// Create a new `Biscuit` by appending an attenuation block
    ///
    /// :param block: a builder for the new block
    /// :type block: BlockBuilder
    /// :return: the attenuated biscuit
    /// :rtype: Biscuit
    pub fn append(&self, block: &PyBlockBuilder) -> PyResult<PyBiscuit> {
        self.0
            .append(block.0.clone().expect("builder already consumed"))
            .map_err(|e| BiscuitBuildError::new_err(e.to_string()))
            .map(PyBiscuit)
    }

    /// Create a new `Biscuit` by appending a third-party attenuation block
    ///
    /// :param external_key: the public key of the third-party that signed the block.
    /// :type external_key: PublicKey
    /// :param block: the third party block to append
    /// :type block: ThirdPartyBlock
    /// :return: the attenuated biscuit
    /// :rtype: Biscuit
    pub fn append_third_party(
        &self,
        external_key: &PyPublicKey,
        block: &PyThirdPartyBlock,
    ) -> PyResult<PyBiscuit> {
        self.0
            .append_third_party(external_key.0, block.0.clone())
            .map_err(|e| BiscuitBuildError::new_err(e.to_string()))
            .map(PyBiscuit)
    }

    /// Create a third-party request for generating third-party blocks.
    ///
    /// :return: the third-party request
    /// :rtype: ThirdPartyRequest
    pub fn third_party_request(&self) -> PyResult<PyThirdPartyRequest> {
        self.0
            .third_party_request()
            .map_err(|e| BiscuitBuildError::new_err(e.to_string()))
            .map(|request| PyThirdPartyRequest(Some(request)))
    }

    /// The revocation ids of the token, encoded as hexadecimal strings
    #[getter]
    pub fn revocation_ids(&self) -> Vec<String> {
        self.0
            .revocation_identifiers()
            .into_iter()
            .map(hex::encode)
            .collect()
    }

    /// Get the external key of a block if it exists
    ///
    /// :param index: the block index
    /// :type index: int
    /// :return: the public key if it exists
    /// :rtype: str | None
    pub fn block_external_key(&self, index: usize) -> PyResult<Option<PyPublicKey>> {
        let opt_key = self
            .0
            .block_external_key(index)
            .map_err(|e| BiscuitBlockError::new_err(e.to_string()))?;

        Ok(opt_key.map(PyPublicKey))
    }

    fn __repr__(&self) -> String {
        self.0.print()
    }
}

/// The Authorizer verifies a request according to its policies and the provided token
///
/// :param source: a datalog snippet
/// :type source: str, optional
/// :param parameters: values for the parameters in the datalog snippet
/// :type parameters: dict, optional
/// :param scope_parameters: public keys for the public key parameters in the datalog snippet
/// :type scope_parameters: dict, optional
#[pyclass(name = "AuthorizerBuilder")]
pub struct PyAuthorizerBuilder(Option<AuthorizerBuilder>);

#[pyclass(name = "AuthorizerLimits")]
#[derive(Clone)]
pub struct PyAuthorizerLimits {
    #[pyo3(get, set)]
    pub max_facts: u64,
    #[pyo3(get, set)]
    pub max_iterations: u64,
    #[pyo3(get, set)]
    pub max_time: Duration,
}

#[pymethods]
impl PyAuthorizerBuilder {
    /// Create a new authorizer from a datalog snippet and optional parameter values
    ///
    /// :param source: a datalog snippet
    /// :type source: str, optional
    /// :param parameters: values for the parameters in the datalog snippet
    /// :type parameters: dict, optional
    /// :param scope_parameters: public keys for the public key parameters in the datalog snippet
    /// :type scope_parameters: dict, optional
    #[new]
    #[pyo3(signature = (source=None, parameters=None, scope_parameters=None))]
    pub fn new(
        source: Option<String>,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<PyAuthorizerBuilder> {
        let mut builder = PyAuthorizerBuilder(Some(AuthorizerBuilder::new()));
        if let Some(source) = source {
            builder.add_code(&source, parameters, scope_parameters)?;
        }
        Ok(builder)
    }

    /// Add code to the builder, using the provided parameters.
    ///
    /// :param source: a datalog snippet
    /// :type source: str, optional
    /// :param parameters: values for the parameters in the datalog snippet
    /// :type parameters: dict, optional
    /// :param scope_parameters: public keys for the public key parameters in the datalog snippet
    /// :type scope_parameters: dict, optional
    #[pyo3(signature = (source, parameters=None, scope_parameters=None))]
    pub fn add_code(
        &mut self,
        source: &str,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<()> {
        let mut params = HashMap::new();

        if let Some(parameters) = parameters {
            for (k, v) in parameters {
                params.insert(k, v.to_term()?);
            }
        }

        let scope_params;

        if let Some(scope_parameters) = scope_parameters {
            scope_params = scope_parameters
                .iter()
                .map(|(k, v)| (k.to_string(), v.0))
                .collect();
        } else {
            scope_params = HashMap::new();
        }

        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .code_with_params(source, params, scope_params)
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single fact to the authorizer. A single fact can be built with
    /// the `Fact` class and its constructor
    ///
    /// :param fact: a datalog fact
    /// :type fact: Fact
    pub fn add_fact(&mut self, fact: &PyFact) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .fact(fact.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single rule to the authorizer. A single rule can be built with
    /// the `Rule` class and its constructor
    ///
    /// :param rule: a datalog rule
    /// :type rule: Rule
    pub fn add_rule(&mut self, rule: &PyRule) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .rule(rule.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single check to the authorizer. A single check can be built with
    /// the `Check` class and its constructor
    ///
    /// :param check: a datalog check
    /// :type check: Check
    pub fn add_check(&mut self, check: &PyCheck) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .check(check.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single policy to the authorizer. A single policy can be built with
    /// the `Policy` class and its constructor
    ///
    /// :param policy: a datalog policy
    /// :type policy: Policy
    pub fn add_policy(&mut self, policy: &PyPolicy) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .policy(policy.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    pub fn limits(&self) -> PyResult<PyAuthorizerLimits> {
        let limits = self
            .0
            .as_ref()
            .expect("builder already consumed")
            .limits()
            .clone();

        Ok(PyAuthorizerLimits {
            max_facts: limits.max_facts,
            max_iterations: limits.max_iterations,
            max_time: Duration::from_std(limits.max_time).expect("Duration out of range"),
        })
    }

    /// Sets the runtime limits of the authorizer
    ///
    /// Those limits cover all the executions under the `authorize`, `query` and `query_all` methods
    pub fn set_limits(&mut self, limits: &PyAuthorizerLimits) -> PyResult<()> {
        self.0 = Some(self.0.take().expect("builder already consumed").set_limits(
            AuthorizerLimits {
                max_facts: limits.max_facts,
                max_iterations: limits.max_iterations,
                max_time: Duration::to_std(&limits.max_time).expect("Duration out of range"),
            },
        ));

        Ok(())
    }

    /// adds a fact `time($current_time)` with the current time
    pub fn set_time(&mut self) -> PyResult<()> {
        self.0 = Some(self.0.take().expect("builder already consumed").time());
        Ok(())
    }

    /// Merge another `Authorizer` in this `Authorizer`. The `Authorizer` argument will not be modified
    ///
    /// :param builder: an Authorizer
    /// :type builder: Authorizer
    pub fn merge(&mut self, builder: &PyAuthorizerBuilder) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .merge(builder.0.clone().expect("builder already consumed")),
        );
        Ok(())
    }

    /// Merge a `BlockBuilder` in this `Authorizer`. The `BlockBuilder` will not be modified
    ///
    /// :param builder: a BlockBuilder
    /// :type builder: BlockBuilder
    pub fn merge_block(&mut self, builder: &PyBlockBuilder) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .merge_block(builder.0.clone().expect("builder already consumed")),
        );
        Ok(())
    }

    pub fn register_extern_func(&mut self, name: &str, func: PyObject) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .register_extern_func(
                    name.to_string(),
                    ExternFunc::new(Arc::new(move |left, right| {
                        Python::with_gil(|py| {
                            let bound = func.bind(py);
                            if bound.is_callable() {
                                let left = term_to_py(&left).map_err(|e| e.to_string())?;
                                let result = match right {
                                    Some(right) => {
                                        let right =
                                            term_to_py(&right).map_err(|e| e.to_string())?;
                                        bound.call1((left, right)).map_err(|e| e.to_string())?
                                    }
                                    None => bound.call1((left,)).map_err(|e| e.to_string())?,
                                };
                                let py_result: PyTerm =
                                    result.extract().map_err(|e| e.to_string())?;
                                Ok(py_result.to_term().map_err(|e| e.to_string())?)
                            } else {
                                Err("expected a function".to_string())
                            }
                        })
                    })),
                ),
        );
        Ok(())
    }

    pub fn register_extern_funcs(&mut self, funcs: HashMap<String, PyObject>) -> PyResult<()> {
        for (name, func) in funcs {
            self.register_extern_func(&name, func)?;
        }

        Ok(())
    }

    pub fn set_extern_funcs(&mut self, funcs: HashMap<String, PyObject>) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .set_extern_funcs(HashMap::new()),
        );
        self.register_extern_funcs(funcs)
    }

    /// Take a snapshot of the authorizer builder and return it, base64-encoded
    ///
    /// :return: a snapshot as a base64-encoded string
    /// :rtype: str
    pub fn base64_snapshot(&self) -> PyResult<String> {
        self.0
            .clone()
            .expect("builder already consumed")
            .to_base64_snapshot()
            .map_err(|error| BiscuitSerializationError::new_err(error.to_string()))
    }

    /// Take a snapshot of the authorizer and return it, as raw bytes
    ///
    /// :return: a snapshot as raw bytes
    /// :rtype: bytes
    pub fn raw_snapshot(&self) -> PyResult<Vec<u8>> {
        self.0
            .clone()
            .expect("builder already consumed")
            .to_raw_snapshot()
            .map_err(|error| BiscuitSerializationError::new_err(error.to_string()))
    }

    /// Build an authorizer builder from a base64-encoded snapshot
    ///
    /// :param input: base64-encoded snapshot
    /// :type input: str
    /// :return: the authorizer builder
    /// :rtype: AuthorizerBuilder
    #[classmethod]
    pub fn from_base64_snapshot(_: &Bound<PyType>, input: &str) -> PyResult<Self> {
        Ok(PyAuthorizerBuilder(Some(
            AuthorizerBuilder::from_base64_snapshot(input)
                .map_err(|error| BiscuitValidationError::new_err(error.to_string()))?,
        )))
    }

    /// Build an authorizer builder from a snapshot's raw bytes
    ///
    /// :param input: raw snapshot bytes
    /// :type input: bytes
    /// :return: the authorizer builder
    /// :rtype: AuthorizerBuilder
    #[classmethod]
    pub fn from_raw_snapshot(_: &Bound<PyType>, input: &[u8]) -> PyResult<Self> {
        Ok(PyAuthorizerBuilder(Some(
            AuthorizerBuilder::from_raw_snapshot(input)
                .map_err(|error| BiscuitValidationError::new_err(error.to_string()))?,
        )))
    }

    /// Build the `AuthorizerBuilder` with the provided `Biscuit`
    ///
    /// :param token: the token to authorize
    /// :type token: Biscuit
    /// :return: the authorizer
    /// :rtype Authorizer
    pub fn build(&self, token: &PyBiscuit) -> PyResult<PyAuthorizer> {
        Ok(PyAuthorizer(
            self.0
                .clone()
                .expect("builder already consumed")
                .build(&token.0)
                .map_err(|e| BiscuitValidationError::new_err(e.to_string()))?,
        ))
    }

    pub fn build_unauthenticated(&self) -> PyResult<PyAuthorizer> {
        Ok(PyAuthorizer(
            self.0
                .clone()
                .expect("builder already consumed")
                .build_unauthenticated()
                .map_err(|e| BiscuitValidationError::new_err(e.to_string()))?,
        ))
    }

    fn __repr__(&self) -> String {
        match self.0 {
            Some(ref x) => x.to_string(),
            None => "_ consumed AuthorizerBuilder _".to_string(),
        }
    }
}

/// The Authorizer verifies a request according to its policies and the provided token
#[pyclass(name = "Authorizer")]
pub struct PyAuthorizer(Authorizer);

#[pymethods]
impl PyAuthorizer {
    /// Runs the authorization checks and policies
    ///
    /// Returns the index of the matching allow policy, or an error containing the matching deny
    /// policy or a list of the failing checks
    ///
    /// :return: the index of the matched allow rule
    /// :rtype: int
    pub fn authorize(&mut self) -> PyResult<usize> {
        self.0
            .authorize()
            .map_err(|error| AuthorizationError::new_err(error.to_string()))
    }

    /// Query the authorizer by returning all the `Fact`s generated by the provided `Rule`. The generated facts won't be
    /// added to the authorizer world.
    ///
    /// This function can be called before `authorize`, but in that case will only return facts that are directly defined,
    /// not the facts generated by rules.
    ///
    /// :param rule: a rule that will be ran against the authorizer contents
    /// :type rule: Rule
    /// :return: a list of generated facts
    /// :rtype: list
    pub fn query(&mut self, rule: &PyRule) -> PyResult<Vec<PyFact>> {
        let results = self
            .0
            .query(rule.0.clone())
            .map_err(|error| AuthorizationError::new_err(error.to_string()))?;

        Ok(results
            .iter()
            .map(|f: &builder::Fact| PyFact(f.clone()))
            .collect())
    }

    /// Take a snapshot of the authorizer and return it, base64-encoded
    ///
    /// :return: a snapshot as a base64-encoded string
    /// :rtype: str
    pub fn base64_snapshot(&self) -> PyResult<String> {
        self.0
            .to_base64_snapshot()
            .map_err(|error| BiscuitSerializationError::new_err(error.to_string()))
    }

    /// Take a snapshot of the authorizer and return it, as raw bytes
    ///
    /// :return: a snapshot as raw bytes
    /// :rtype: bytes
    pub fn raw_snapshot(&self) -> PyResult<Vec<u8>> {
        self.0
            .to_raw_snapshot()
            .map_err(|error| BiscuitSerializationError::new_err(error.to_string()))
    }

    /// Build an authorizer from a base64-encoded snapshot
    ///
    /// :param input: base64-encoded snapshot
    /// :type input: str
    /// :return: the authorizer
    /// :rtype: Authorizer
    #[classmethod]
    pub fn from_base64_snapshot(_: &Bound<PyType>, input: &str) -> PyResult<Self> {
        Ok(PyAuthorizer(
            Authorizer::from_base64_snapshot(input)
                .map_err(|error| BiscuitValidationError::new_err(error.to_string()))?,
        ))
    }

    /// Build an authorizer from a snapshot's raw bytes
    ///
    /// :param input: raw snapshot bytes
    /// :type input: bytes
    /// :return: the authorizer
    /// :rtype: Authorizer
    #[classmethod]
    pub fn from_raw_snapshot(_: &Bound<PyType>, input: &[u8]) -> PyResult<Self> {
        Ok(PyAuthorizer(Authorizer::from_raw_snapshot(input).map_err(
            |error| BiscuitValidationError::new_err(error.to_string()),
        )?))
    }

    fn __repr__(&self) -> String {
        self.0.to_string()
    }
}

/// Builder class allowing to create a block meant to be appended to an existing token
///
/// :param source: a datalog snippet
/// :type source: str, optional
/// :param parameters: values for the parameters in the datalog snippet
/// :type parameters: dict, optional
/// :param scope_parameters: public keys for the public key parameters in the datalog snippet
/// :type scope_parameters: dict, optional
#[pyclass(name = "BlockBuilder")]
#[derive(Clone)]
pub struct PyBlockBuilder(Option<builder::BlockBuilder>);

#[pymethods]
impl PyBlockBuilder {
    /// Create a builder from a datalog snippet and optional parameter values
    ///
    /// :param source: a datalog snippet
    /// :type source: str, optional
    /// :param parameters: values for the parameters in the datalog snippet
    /// :type parameters: dict, optional
    /// :param scope_parameters: public keys for the public key parameters in the datalog snippet
    /// :type scope_parameters: dict, optional
    #[new]
    #[pyo3(signature = (source=None, parameters=None, scope_parameters=None))]
    fn new(
        source: Option<String>,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<PyBlockBuilder> {
        let mut builder = PyBlockBuilder(Some(builder::BlockBuilder::new()));
        if let Some(source) = source {
            builder.add_code(&source, parameters, scope_parameters)?;
        }
        Ok(builder)
    }

    /// Add a single fact to the builder. A single fact can be built with
    /// the `Fact` class and its constructor
    ///
    /// :param fact: a datalog fact
    /// :type fact: Fact
    pub fn add_fact(&mut self, fact: &PyFact) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .fact(fact.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single rule to the builder. A single rule can be built with
    /// the `Rule` class and its constructor
    ///
    /// :param rule: a datalog rule
    /// :type rule: Rule
    pub fn add_rule(&mut self, rule: &PyRule) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .rule(rule.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Add a single check to the builder. A single check can be built with
    /// the `Check` class and its constructor
    ///
    /// :param check: a datalog check
    /// :type check: Check
    pub fn add_check(&mut self, check: &PyCheck) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .check(check.0.clone())
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );

        Ok(())
    }

    /// Merge a `BlockBuilder` in this `BlockBuilder`. The `BlockBuilder` will not be modified
    ///
    /// :param builder: a datalog BlockBuilder
    /// :type builder: BlockBuilder
    pub fn merge(&mut self, builder: &mut PyBlockBuilder) -> PyResult<()> {
        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .merge(builder.0.take().expect("builder already consumed")),
        );
        Ok(())
    }

    /// Add code to the builder, using the provided parameters.
    ///
    /// :param source: a datalog snippet
    /// :type source: str, optional
    /// :param parameters: values for the parameters in the datalog snippet
    /// :type parameters: dict, optional
    /// :param scope_parameters: public keys for the public key parameters in the datalog snippet
    /// :type scope_parameters: dict, optional
    #[pyo3(signature = (source, parameters=None, scope_parameters=None))]
    pub fn add_code(
        &mut self,
        source: &str,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<()> {
        let mut params = HashMap::new();

        if let Some(parameters) = parameters {
            for (k, v) in parameters {
                params.insert(k, v.to_term()?);
            }
        }

        let scope_params;

        if let Some(scope_parameters) = scope_parameters {
            scope_params = scope_parameters
                .iter()
                .map(|(k, v)| (k.to_string(), v.0))
                .collect();
        } else {
            scope_params = HashMap::new();
        }

        self.0 = Some(
            self.0
                .take()
                .expect("builder already consumed")
                .code_with_params(source, params, scope_params)
                .map_err(|e| DataLogError::new_err(e.to_string()))?,
        );
        Ok(())
    }

    fn __repr__(&self) -> String {
        match self.0 {
            Some(ref b) => b.to_string(),
            None => "_ BlockBuilder already consumed _".to_string(),
        }
    }
}

/// Third party block request
#[pyclass(name = "ThirdPartyRequest")]
pub struct PyThirdPartyRequest(Option<ThirdPartyRequest>);

#[pymethods]
impl PyThirdPartyRequest {
    /// Create a third-party block
    ///
    /// :param private_key: the third-party's private key used to sign the block
    /// :type external_key: PrivateKey
    /// :param block: the block builder to be signed
    /// :type block: BlockBuilder
    /// :return: a signed block that can be appended to a Biscuit
    /// :rtype: ThirdPartyBlock
    ///
    /// :note: this method consumes the `ThirdPartyRequest` object.
    pub fn create_block(
        &mut self,
        private_key: &PyPrivateKey,
        block: &PyBlockBuilder,
    ) -> PyResult<PyThirdPartyBlock> {
        self.0
            .take()
            .expect("third party request already consumed")
            .create_block(
                &private_key.0,
                block.0.clone().expect("builder already consumed"),
            )
            .map_err(|e| BiscuitBuildError::new_err(e.to_string()))
            .map(PyThirdPartyBlock)
    }
}

/// Third party block contents
#[pyclass(name = "ThirdPartyBlock")]
pub struct PyThirdPartyBlock(ThirdPartyBlock);

/// ed25519 keypair
#[pyclass(name = "KeyPair")]
pub struct PyKeyPair(KeyPair);

#[pymethods]
impl PyKeyPair {
    /// Generate a random keypair
    #[new]
    pub fn new() -> Self {
        PyKeyPair(KeyPair::new())
    }

    /// Generate a keypair from a private key
    ///
    /// :param private_key: the private key
    /// :type private_key: PrivateKey
    /// :return: the corresponding keypair
    /// :rtype: KeyPair
    #[classmethod]
    pub fn from_private_key(_: &Bound<PyType>, private_key: PyPrivateKey) -> Self {
        PyKeyPair(KeyPair::from(&private_key.0))
    }

    /// The public key part
    #[getter]
    pub fn public_key(&self) -> PyPublicKey {
        PyPublicKey(self.0.public())
    }

    /// The private key part
    #[getter]
    pub fn private_key(&self) -> PyPrivateKey {
        PyPrivateKey(self.0.private())
    }
}

impl Default for PyKeyPair {
    fn default() -> Self {
        Self::new()
    }
}

/// ed25519 public key
#[derive(Clone)]
#[pyclass(name = "PublicKey")]
pub struct PyPublicKey(PublicKey);

#[pymethods]
impl PyPublicKey {
    /// Serializes a public key to raw bytes
    ///
    /// :return: the public key bytes
    /// :rtype: list
    pub fn to_bytes(&self) -> Vec<u8> {
        self.0.to_bytes()
    }

    /// Serializes a public key to a hexadecimal string
    ///
    /// :return: the public key bytes (hex-encoded)
    /// :rtype: str
    fn __repr__(&self) -> String {
        self.0.to_string()
    }

    /// Deserializes a public key from raw bytes
    ///
    /// :param data: the raw bytes
    /// :type data: bytes
    /// :return: the public key
    /// :rtype: PublicKey
    #[classmethod]
    pub fn from_bytes(_: &Bound<PyType>, data: &[u8], alg: &PyAlgorithm) -> PyResult<PyPublicKey> {
        match PublicKey::from_bytes(data, builder::Algorithm::from(*alg)) {
            Ok(key) => Ok(PyPublicKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }

    /// Deserializes a public key from a hexadecimal string
    ///
    /// :param data: the hex-encoded string
    /// :type data: str
    /// :return: the public key
    /// :rtype: PublicKey
    #[new]
    pub fn new(data: &str) -> PyResult<PyPublicKey> {
        match PublicKey::from_str(data) {
            Ok(key) => Ok(PyPublicKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }

    /// Deserializes a public key from a der buffer
    ///
    /// :param der: the der buffer
    /// :type der: bytes
    /// :return: the public key
    /// :rtype: PublicKey
    #[classmethod]
    pub fn from_der(_: &Bound<PyType>, der: &[u8]) -> PyResult<Self> {
        match PublicKey::from_der(der) {
            Ok(key) => Ok(PyPublicKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }

    /// Deserializes a public key from a PEM string
    ///
    /// :param data: the der buffer
    /// :type pem: string
    /// :return: the public key
    /// :rtype: PublicKey
    #[classmethod]
    pub fn from_pem(_: &Bound<PyType>, pem: &str) -> PyResult<Self> {
        match PublicKey::from_pem(pem) {
            Ok(key) => Ok(PyPublicKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }
}

/// ed25519 private key
#[pyclass(name = "PrivateKey")]
#[derive(Clone)]
pub struct PyPrivateKey(PrivateKey);

#[pymethods]
impl PyPrivateKey {
    /// Serializes a public key to raw bytes
    ///
    /// :return: the public key bytes
    /// :rtype: list
    pub fn to_bytes(&self) -> Vec<u8> {
        self.0.to_bytes().deref().clone()
    }

    /// Serializes a private key to a hexadecimal string
    ///
    /// :return: the private key bytes (hex-encoded)
    /// :rtype: str
    fn __repr__(&self) -> String {
        self.0.to_prefixed_string()
    }

    /// Deserializes a private key from raw bytes
    ///
    /// :param data: the raw bytes
    /// :type data: bytes
    /// :return: the private key
    /// :rtype: PrivateKey
    #[classmethod]
    pub fn from_bytes(_: &Bound<PyType>, data: &[u8], alg: &PyAlgorithm) -> PyResult<PyPrivateKey> {
        match PrivateKey::from_bytes(data, builder::Algorithm::from(*alg)) {
            Ok(key) => Ok(PyPrivateKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }

    /// Deserializes a private key from a hexadecimal string
    ///
    /// :param data: the hex-encoded string
    /// :type data: str
    /// :return: the private key
    /// :rtype: PrivateKey
    #[new]
    pub fn new(data: &str) -> PyResult<PyPrivateKey> {
        match PrivateKey::from_str(data) {
            Ok(key) => Ok(PyPrivateKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }

    /// Deserializes a private key from a der buffer
    ///
    /// :param der: the der buffer
    /// :type der: bytes
    /// :return: the Private key
    /// :rtype: PrivateKey
    #[classmethod]
    pub fn from_der(_: &Bound<PyType>, der: &[u8]) -> PyResult<Self> {
        match PrivateKey::from_der(der) {
            Ok(key) => Ok(PyPrivateKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }

    /// Deserializes a private key from a PEM string
    ///
    /// :param data: the der buffer
    /// :type pem: string
    /// :return: the Private key
    /// :rtype: PrivateKey
    #[classmethod]
    pub fn from_pem(_: &Bound<PyType>, pem: &str) -> PyResult<Self> {
        match PrivateKey::from_pem(pem) {
            Ok(key) => Ok(PyPrivateKey(key)),
            Err(error) => Err(PyValueError::new_err(error.to_string())),
        }
    }
}

/// Datalog term that can occur in a set
#[derive(PartialEq, Eq, PartialOrd, Ord, FromPyObject)]
pub enum NestedPyTerm {
    Bool(bool),
    Integer(i64),
    Str(String),
    Date(PyDate),
    Bytes(Vec<u8>),
}

// TODO follow up-to-date conversion methods from pyo3
fn inner_term_to_py(t: &builder::Term, py: Python<'_>) -> PyResult<Py<PyAny>> {
    match t {
        builder::Term::Integer(i) => Ok((*i).into_pyobject(py).unwrap().into_any().unbind()),
        builder::Term::Str(s) => Ok(s.into_pyobject(py).unwrap().into_any().unbind()),
        builder::Term::Date(d) => Ok(Utc
            .timestamp_opt(*d as i64, 0)
            .unwrap()
            .into_pyobject(py)
            .unwrap()
            .into_any()
            .unbind()),
        builder::Term::Bytes(bs) => Ok(bs.clone().into_pyobject(py).unwrap().into_any().unbind()),
        builder::Term::Bool(b) => Ok(b.into_py(py)),
        _ => Err(DataLogError::new_err("Invalid term value".to_string())),
    }
}

fn term_to_py(t: &builder::Term) -> PyResult<Py<PyAny>> {
    Python::with_gil(|py| match t {
        builder::Term::Parameter(_) => Err(DataLogError::new_err("Invalid term value".to_string())),
        builder::Term::Variable(_) => Err(DataLogError::new_err("Invalid term value".to_string())),
        builder::Term::Set(_vs) => todo!(),
        builder::Term::Array(_vs) => todo!(),
        builder::Term::Map(_vs) => todo!(),
        term => inner_term_to_py(term, py),
    })
}

/// Wrapper for a non-naïve python date
#[derive(FromPyObject)]
pub struct PyDate(Py<PyDateTime>);

impl PartialEq for PyDate {
    fn eq(&self, other: &Self) -> bool {
        self.0.to_string() == other.0.to_string()
    }
}

impl Eq for PyDate {}

impl PartialOrd for PyDate {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for PyDate {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.0.to_string().cmp(&other.0.to_string())
    }
}

/// Term values passed from python-land.
#[derive(FromPyObject)]
pub enum PyTerm {
    Simple(NestedPyTerm),
    Set(BTreeSet<NestedPyTerm>),
    Array(Vec<PyTerm>),
    StrDict(HashMap<String, PyTerm>),
    IntDict(HashMap<i64, PyTerm>),
}

impl NestedPyTerm {
    pub fn to_term(&self) -> PyResult<builder::Term> {
        match self {
            NestedPyTerm::Integer(i) => Ok((*i).into()),
            NestedPyTerm::Str(s) => Ok(builder::Term::Str(s.to_string())),
            NestedPyTerm::Bytes(b) => Ok(b.clone().into()),
            NestedPyTerm::Bool(b) => Ok((*b).into()),
            NestedPyTerm::Date(PyDate(d)) => Python::with_gil(|py| {
                let ts = d.extract::<DateTime<Utc>>(py)?.timestamp();
                if ts < 0 {
                    return Err(PyValueError::new_err(
                        "Only positive timestamps are available".to_string(),
                    ));
                }
                Ok(builder::Term::Date(ts as u64))
            }),
        }
    }
}

impl PyTerm {
    pub fn to_term(&self) -> PyResult<builder::Term> {
        match self {
            PyTerm::Simple(s) => s.to_term(),
            PyTerm::Set(vs) => vs
                .iter()
                .map(|s| s.to_term())
                .collect::<PyResult<_>>()
                .map(builder::Term::Set),
            PyTerm::Array(vs) => vs
                .iter()
                .map(|s| s.to_term())
                .collect::<PyResult<_>>()
                .map(builder::Term::Array),
            PyTerm::StrDict(vs) => vs
                .iter()
                .map(|(k, v)| Ok((MapKey::Str(k.to_string()), v.to_term()?)))
                .collect::<PyResult<_>>()
                .map(builder::Term::Map),
            PyTerm::IntDict(vs) => vs
                .iter()
                .map(|(k, v)| Ok((MapKey::Integer(*k), v.to_term()?)))
                .collect::<PyResult<_>>()
                .map(builder::Term::Map),
        }
    }
}

/// A single datalog Fact
///
/// :param source: a datalog fact (without the ending semicolon)
/// :type source: str
/// :param parameters: values for the parameters in the datalog fact
/// :type parameters: dict, optional
#[pyclass(name = "Fact")]
pub struct PyFact(builder::Fact);

#[pymethods]
impl PyFact {
    /// Build a datalog fact from the provided source and optional parameter values
    #[new]
    #[pyo3(signature = (source, parameters=None))]
    pub fn new(source: &str, parameters: Option<HashMap<String, PyTerm>>) -> PyResult<Self> {
        let mut fact: builder::Fact = source
            .try_into()
            .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
        if let Some(parameters) = parameters {
            for (k, v) in parameters {
                fact.set(&k, v.to_term()?)
                    .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
            }
        }
        Ok(PyFact(fact))
    }

    /// The fact name
    #[getter]
    pub fn name(&self) -> String {
        self.0.predicate.name.clone()
    }

    /// The fact terms
    #[getter]
    pub fn terms(&self) -> PyResult<Vec<PyObject>> {
        self.0.predicate.terms.iter().map(term_to_py).collect()
    }

    fn __repr__(&self) -> String {
        self.0.to_string()
    }
}

/// A single datalog rule
///
/// :param source: a datalog rule (without the ending semicolon)
/// :type source: str
/// :param parameters: values for the parameters in the datalog rule
/// :type parameters: dict, optional
/// :param scope_parameters: public keys for the public key parameters in the datalog rule
/// :type scope_parameters: dict, optional
#[pyclass(name = "Rule")]
pub struct PyRule(builder::Rule);

#[pymethods]
impl PyRule {
    /// Build a rule from the source and optional parameter values
    #[new]
    #[pyo3(signature = (source, parameters=None, scope_parameters=None))]
    pub fn new(
        source: &str,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<Self> {
        let mut rule: builder::Rule = source
            .try_into()
            .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
        if let Some(parameters) = parameters {
            for (k, v) in parameters {
                rule.set(&k, v.to_term()?)
                    .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
            }
        }

        if let Some(scope_parameters) = scope_parameters {
            for (k, v) in scope_parameters {
                rule.set_scope(&k, v.0)
                    .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
            }
        }
        Ok(PyRule(rule))
    }

    fn __repr__(&self) -> String {
        self.0.to_string()
    }
}

/// A single datalog check
///
/// :param source: a datalog check (without the ending semicolon)
/// :type source: str
/// :param parameters: values for the parameters in the datalog check
/// :type parameters: dict, optional
/// :param scope_parameters: public keys for the public key parameters in the datalog check
/// :type scope_parameters: dict, optional
#[pyclass(name = "Check")]
pub struct PyCheck(builder::Check);

#[pymethods]
impl PyCheck {
    /// Build a check from the source and optional parameter values
    #[pyo3(signature = (source, parameters=None, scope_parameters=None))]
    #[new]
    pub fn new(
        source: &str,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<Self> {
        let mut check: builder::Check = source
            .try_into()
            .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
        if let Some(parameters) = parameters {
            for (k, v) in parameters {
                check
                    .set(&k, v.to_term()?)
                    .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
            }
        }

        if let Some(scope_parameters) = scope_parameters {
            for (k, v) in scope_parameters {
                check
                    .set_scope(&k, v.0)
                    .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
            }
        }
        Ok(PyCheck(check))
    }

    fn __repr__(&self) -> String {
        self.0.to_string()
    }
}

/// A single datalog policy
///
/// :param source: a datalog policy (without the ending semicolon)
/// :type source: str
/// :param parameters: values for the parameters in the datalog policy
/// :type parameters: dict, optional
/// :param scope_parameters: public keys for the public key parameters in the datalog policy
/// :type scope_parameters: dict, optional
#[pyclass(name = "Policy")]
pub struct PyPolicy(builder::Policy);

#[pymethods]
impl PyPolicy {
    /// Build a check from the source and optional parameter values
    #[new]
    #[pyo3(signature = (source, parameters=None, scope_parameters=None))]
    pub fn new(
        source: &str,
        parameters: Option<HashMap<String, PyTerm>>,
        scope_parameters: Option<HashMap<String, PyPublicKey>>,
    ) -> PyResult<Self> {
        let mut policy: builder::Policy = source
            .try_into()
            .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
        if let Some(parameters) = parameters {
            for (k, v) in parameters {
                policy
                    .set(&k, v.to_term()?)
                    .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
            }
        }

        if let Some(scope_parameters) = scope_parameters {
            for (k, v) in scope_parameters {
                policy
                    .set_scope(&k, v.0)
                    .map_err(|e: error::Token| DataLogError::new_err(e.to_string()))?;
            }
        }
        Ok(PyPolicy(policy))
    }

    fn __repr__(&self) -> String {
        self.0.to_string()
    }
}

/// Representation of a biscuit token that has been parsed but not cryptographically verified
#[pyclass(name = "UnverifiedBiscuit")]
pub struct PyUnverifiedBiscuit(UnverifiedBiscuit);

#[pymethods]
impl PyUnverifiedBiscuit {
    /// Deserializes a token from URL safe base 64 data
    ///
    /// The signature will NOT be checked
    ///
    /// :param data: a (url-safe) base64-encoded string
    /// :type data: str
    /// :return: the parsed, unverified biscuit
    /// :rtype: UnverifiedBiscuit
    #[classmethod]
    pub fn from_base64(_: &Bound<PyType>, data: &str) -> PyResult<PyUnverifiedBiscuit> {
        match UnverifiedBiscuit::from_base64(data) {
            Ok(biscuit) => Ok(PyUnverifiedBiscuit(biscuit)),
            Err(error) => Err(BiscuitValidationError::new_err(error.to_string())),
        }
    }

    /// Returns the root key identifier for this `UnverifiedBiscuit` (or `None` if there is none)
    ///
    /// :return: the root key identifier
    /// :rtype: int
    pub fn root_key_id(&self) -> Option<u32> {
        self.0.root_key_id()
    }

    /// Returns the number of blocks in the token
    ///
    /// :return: the number of blocks
    /// :rtype: int
    pub fn block_count(&self) -> usize {
        self.0.block_count()
    }

    /// Prints a block's content as Datalog code
    ///
    /// :param index: the block index
    /// :type index: int
    /// :return: the code for the corresponding block
    /// :rtype: str
    pub fn block_source(&self, index: usize) -> PyResult<String> {
        self.0
            .print_block_source(index)
            .map_err(|e| BiscuitBlockError::new_err(e.to_string()))
    }

    /// Create a new `UnverifiedBiscuit` by appending an attenuation block
    ///
    /// :param block: a builder for the new block
    /// :type block: BlockBuilder
    /// :return: the attenuated biscuit
    /// :rtype: Biscuit
    pub fn append(&self, block: &PyBlockBuilder) -> PyResult<PyUnverifiedBiscuit> {
        self.0
            .append(block.0.clone().expect("builder already consumed"))
            .map_err(|e| BiscuitBuildError::new_err(e.to_string()))
            .map(PyUnverifiedBiscuit)
    }

    /// The revocation ids of the token, encoded as hexadecimal strings
    #[getter]
    pub fn revocation_ids(&self) -> Vec<String> {
        self.0
            .revocation_identifiers()
            .into_iter()
            .map(hex::encode)
            .collect()
    }

    pub fn verify(&self, root: PyObject) -> PyResult<PyBiscuit> {
        Ok(PyBiscuit(
            self.0
                .clone()
                .verify(PyKeyProvider { py_value: root })
                .map_err(|e| BiscuitValidationError::new_err(e.to_string()))?,
        ))
    }
}

/// Main module for the biscuit_auth lib
#[pymodule]
pub fn biscuit_auth(py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    m.add_class::<PyKeyPair>()?;
    m.add_class::<PyPublicKey>()?;
    m.add_class::<PyPrivateKey>()?;
    m.add_class::<PyBiscuit>()?;
    m.add_class::<PyBiscuitBuilder>()?;
    m.add_class::<PyBlockBuilder>()?;
    m.add_class::<PyAuthorizer>()?;
    m.add_class::<PyAuthorizerBuilder>()?;
    m.add_class::<PyFact>()?;
    m.add_class::<PyRule>()?;
    m.add_class::<PyCheck>()?;
    m.add_class::<PyPolicy>()?;
    m.add_class::<PyUnverifiedBiscuit>()?;
    m.add_class::<PyAlgorithm>()?;
    m.add_class::<PyThirdPartyRequest>()?;
    m.add_class::<PyThirdPartyBlock>()?;

    m.add("DataLogError", py.get_type::<DataLogError>())?;
    m.add("AuthorizationError", py.get_type::<AuthorizationError>())?;
    m.add("BiscuitBuildError", py.get_type::<BiscuitBuildError>())?;
    m.add("BiscuitBlockError", py.get_type::<BiscuitBlockError>())?;
    m.add(
        "BiscuitValidationError",
        py.get_type::<BiscuitValidationError>(),
    )?;
    m.add(
        "BiscuitSerializationError",
        py.get_type::<BiscuitSerializationError>(),
    )?;

    Ok(())
}
