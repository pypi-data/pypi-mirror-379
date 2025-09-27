use thiserror::Error;


#[derive(Debug, Error)]
pub enum Error {
    #[error("io error: {0}")]
    IO(#[from] std::io::Error),
    #[error("could not parse color: {0}")]
    ColorParse(String),
    #[error("colorcet error: {0}")]
    ColorCet(#[from] colorcet::ColorcetError),
    #[error("could not covert ColorMap into LinearGradient")]
    Conversion
}