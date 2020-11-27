use float_cmp::*;
use std::error::Error;
use std::fmt;
use std::ops::{Add, Div, Mul, Neg, Sub};
pub const EPSILON: f64 = 0.000001;

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

    pub fn magnitude(&self) -> f64 {
        (self.x.powf(2.0) + self.y.powf(2.0) + self.z.powf(2.0) + self.w.powf(2.0)).sqrt()
    }

    pub fn normalize(&self) -> Self {
        let mag = self.magnitude();
        Self {
            x: self.x / mag,
            y: self.y / mag,
            z: self.z / mag,
            w: self.w / mag,
        }
    }

    pub fn dot(&self, other: &Self) -> f64 {
        self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w
    }

    pub fn cross(&self, other: &Self) -> Self {
        Tuple::vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )
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
    type Output = Self;

    fn add(self, other: Self) -> Self {
        let out = Self {
            x: self.x + other.x,
            y: self.y + other.y,
            z: self.z + other.z,
            w: self.w + other.w,
        };

        if out.w > 1.0 {
            panic!("Point + Point addition is not valid");
        } else {
            out
        }
    }
}

impl Sub for Tuple {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        let out = Self {
            x: self.x - other.x,
            y: self.y - other.y,
            z: self.z - other.z,
            w: self.w - other.w,
        };

        if out.w < 0.0 {
            panic!("Vector - Point subtractin is not valid");
        } else {
            out
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

impl Mul<f64> for Tuple {
    type Output = Self;
    fn mul(self, other: f64) -> Self {
        Self {
            x: self.x * other,
            y: self.y * other,
            z: self.z * other,
            w: self.w * other,
        }
    }
}

impl Div<f64> for Tuple {
    type Output = Self;

    fn div(self, other: f64) -> Self {
        Self {
            x: self.x / other,
            y: self.y / other,
            z: self.z / other,
            w: self.w / other,
        }
    }
}
