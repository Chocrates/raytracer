mod other;

pub mod prelude {
    pub use crate::other::*;
}

use prelude::*;

fn main() {
    println!("test");
    let test_var = Hello::new();
    println!("{}", test_var.run());
}
