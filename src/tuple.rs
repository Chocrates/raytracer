use float_cmp::*;
use std::error::Error;
use std::fmt;
use std::ops::{Add, Neg, Sub};
pub const EPSILON: f64 = 0.0001;

#[derive(Debug)]
pub struct Tuple {
    pub x: f64,
    pub y: f64,
    pub z: f64,
    pub w: f64,
}

#[derive(Debug)]
pub struct TupleError {}
impl fmt::Display for TupleError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Invalid Tuple types")
    }
}

impl Error for TupleError {}

impl Tuple {
    pub fn new(x: f64, y: f64, z: f64, w: f64) -> Self {
        Self {
            x: x,
            y: y,
            z: z,
            w: w,
        }
    }

    pub fn point(x: f64, y: f64, z: f64) -> Self {
        Tuple::new(x, y, z, 1.0)
    }

    pub fn vector(x: f64, y: f64, z: f64) -> Self {
        Tuple::new(x, y, z, 0.0)
    }

    pub fn is_point(&self) -> bool {
        approx_eq!(f64, self.w, 1.0, epsilon = EPSILON)
    }

    pub fn is_vector(&self) -> bool {
        approx_eq!(f64, self.w, 0.0, epsilon = EPSILON)
    }
}

impl fmt::Display for Tuple {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "Tuple(x:{}, y:{}, z:{}, w:{})",
            self.x, self.y, self.z, self.w
        )
    }
}
impl Add for Tuple {
    type Output = Result<Self, TupleError>;

    fn add(self, other: Self) -> Result<Self, TupleError> {
        let out = Self {
            x: self.x + other.x,
            y: self.y + other.y,
            z: self.z + other.z,
            w: self.w + other.w,
        };

        if out.w > 1.0 {
            Err(TupleError {})
        } else {
            Ok(out)
        }
    }
}

impl Sub for Tuple {
    type Output = Result<Self, TupleError>;

    fn sub(self, other: Self) -> Result<Self, TupleError> {
        let out = Self {
            x: self.x - other.x,
            y: self.y - other.y,
            z: self.z - other.z,
            w: self.w - other.w,
        };

        if out.w < 0.0 {
            Err(TupleError {})
        } else {
            Ok(out)
        }
    }
}

impl Neg for Tuple {
    type Output = Self;
    fn neg(self) -> Self {
        Self {
            x: -self.x,
            y: -self.y,
            z: -self.z,
            w: -self.w,
        }
    }
}
