use quick_xml::DeError;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum Error {
    #[error("io error: {0}")]
    IO(#[from] std::io::Error),
    #[error("serde error: {0}")]
    SerdeXml(#[from] DeError),
    #[error("size of {0} is unknown")]
    SizeOfUnknown(String),
    #[error("no conversion to K by multiplication only")]
    TemparatureConversion,
}
