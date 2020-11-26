extern crate raytracer;
use raytracer::*;

use regex::Regex;

pub fn main() {
    println!("test");

    println!("{}", (tuple::Tuple::vector(1.0, -2.0, 3.0) / 2.0));
    println!("{}", (tuple::Tuple::vector(1.0, -2.0, 3.0) * 0.5));
    println!("{}", (tuple::Tuple::vector(1.0, 0.0, 1.0)).magnitude());
    println!(
        "{}",
        (tuple::Tuple::vector(1.0, 2.0, 3.0))
            .normalize()
            .magnitude()
    );

    println!(
        "{}",
        tuple::Tuple::vector(1.0, 2.0, 3.0).dot(tuple::Tuple::vector(2.0, 3.0, 4.0))
    );

    println!(
        "{}",
        tuple::Tuple::vector(1.0, 2.0, 3.0).cross(tuple::Tuple::vector(2.0, 3.0, 4.0))
    );

    println!(
        "{}",
        tuple::Tuple::vector(2.0, 3.0, 4.0).cross(tuple::Tuple::vector(1.0, 2.0, 3.0))
    );
}
