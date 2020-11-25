pub use crate::prelude::*;

#[derive(PartialEq)]
pub struct Hello {}

impl Hello {
    pub fn new() -> Hello {
        Hello {}
    }

    pub fn run(&self) -> String {
        String::from("Hello World!")
    }
}
