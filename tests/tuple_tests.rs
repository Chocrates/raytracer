use float_cmp::*;
use raytracer::*;

fn validate_tuple(tuple: &tuple::Tuple, x: f64, y: f64, z: f64, w: f64) -> bool {
    approx_eq!(f64, tuple.x, x, epsilon = tuple::EPSILON)
        && approx_eq!(f64, tuple.y, y, epsilon = tuple::EPSILON)
        && approx_eq!(f64, tuple.z, z, epsilon = tuple::EPSILON)
        && approx_eq!(f64, tuple.w, w, epsilon = tuple::EPSILON)
}

#[test]
fn test_tuple_is_point() {
    let a = tuple::Tuple::new(4.3, -4.2, 3.1, 1.0);
    assert!(validate_tuple(&a, 4.3, -4.2, 3.1, 1.0));
    assert_eq!(a.is_point(), true);
    assert_eq!(a.is_vector(), false);
}

#[test]
fn test_tuple_is_vector() {
    let a = tuple::Tuple::new(4.3, -4.2, 3.1, 0.0);
    assert!(validate_tuple(&a, 4.3, -4.2, 3.1, 0.0));
    assert_eq!(a.is_point(), false);
    assert_eq!(a.is_vector(), true);
}

#[test]
fn test_point_is_point() {
    let a = tuple::Tuple::point(4.0, -4.0, 3.0);
    assert!(validate_tuple(&a, 4.0, -4.0, 3.0, 1.0));
    assert_eq!(a.is_point(), true);
    assert_eq!(a.is_vector(), false);
}

#[test]
fn test_vector_is_vector() {
    let a = tuple::Tuple::vector(4.0, -4.0, 3.0);
    assert!(validate_tuple(&a, 4.0, -4.0, 3.0, 0.0));
    assert_eq!(a.is_point(), false);
    assert_eq!(a.is_vector(), true);
}

#[test]
fn test_vector_addition() {
    let a = tuple::Tuple::new(3.0, -2.0, 5.0, 1.0);
    let b = tuple::Tuple::new(-2.0, 3.0, 1.0, 0.0);
    let c = a + b;
    assert!(validate_tuple(&c, 1.0, 1.0, 6.0, 1.0));
}

#[test]
fn test_point_point_subtraction() {
    let a = tuple::Tuple::point(3.0, 2.0, 1.0);
    let b = tuple::Tuple::point(5.0, 6.0, 7.0);
    let c = a - b;
    assert!(validate_tuple(&c, -2.0, -4.0, -6.0, 0.0));
}

#[test]
fn test_vector_point_subtraction() {
    let a = tuple::Tuple::point(3.0, 2.0, 1.0);
    let b = tuple::Tuple::vector(5.0, 6.0, 7.0);
    let c = a - b;
    assert!(validate_tuple(&c, -2.0, -4.0, -6.0, 1.0));
}

#[test]
fn test_vector_vector_subtraction() {
    let a = tuple::Tuple::vector(3.0, 2.0, 1.0);
    let b = tuple::Tuple::vector(5.0, 6.0, 7.0);
    let c = a - b;
    assert!(validate_tuple(&c, -2.0, -4.0, -6.0, 0.0));
}

#[test]
fn test_zero_vector_vector_subtraction() {
    let a = tuple::Tuple::vector(0.0, 0.0, 0.0);
    let b = tuple::Tuple::vector(1.0, -2.0, 3.0);
    let c = a - b;
    assert!(validate_tuple(&c, -1.0, 2.0, -3.0, 0.0));
}

#[test]
fn test_negate_tuple() {
    let a = tuple::Tuple::new(1.0, -2.0, 3.0, -4.0);
    let b = -a;
    assert!(validate_tuple(&b, -1.0, 2.0, -3.0, 4.0));
}

#[test]
fn test_multiply_scalar() {
    let a = tuple::Tuple::new(1.0, -2.0, 3.0, -4.0);
    let b = a * 3.5;
    assert!(validate_tuple(&b, 3.5, -7.0, 10.5, -14.0));
}

#[test]
fn test_multiply_fraction() {
    let a = tuple::Tuple::new(1.0, -2.0, 3.0, -4.0);
    let b = a * 0.5;
    assert!(validate_tuple(&b, 0.5, -1.0, 1.5, -2.0));
}

#[test]
fn test_divide_scalar() {
    let a = tuple::Tuple::new(1.0, -2.0, 3.0, -4.0);
    let b = a / 2.0;
    assert!(validate_tuple(&b, 0.5, -1.0, 1.5, -2.0));
}

#[test]
fn test_compute_magnitude1() {
    let a = tuple::Tuple::vector(1.0, 0.0, 0.0);
    assert!(approx_eq!(
        f64,
        a.magnitude(),
        1.0,
        epsilon = tuple::EPSILON
    ));
}

#[test]
fn test_compute_magnitude2() {
    let a = tuple::Tuple::vector(0.0, 1.0, 0.0);
    assert!(approx_eq!(
        f64,
        a.magnitude(),
        1.0,
        epsilon = tuple::EPSILON
    ));
}

#[test]
fn test_compute_magnitude3() {
    let a = tuple::Tuple::vector(0.0, 0.0, 1.0);
    assert!(approx_eq!(
        f64,
        a.magnitude(),
        1.0,
        epsilon = tuple::EPSILON
    ));
}

#[test]
fn test_compute_magnitude4() {
    let a = tuple::Tuple::vector(-1.0, -2.0, -3.0);
    assert!(approx_eq!(
        f64,
        a.magnitude(),
        f64::sqrt(14.0),
        epsilon = tuple::EPSILON
    ));
}

#[test]
fn test_normalize_vector1() {
    let a = tuple::Tuple::vector(4.0, 0.0, 0.0);
    assert!(validate_tuple(&a.normalize(), 1.0, 0.0, 0.0, 0.0));
}

#[test]
fn test_normalize_vector2() {
    let a = tuple::Tuple::vector(1.0, 2.0, 3.0);
    assert!(validate_tuple(
        &a.normalize(),
        1.0 / f64::sqrt(14.0),
        2.0 / f64::sqrt(14.0),
        3.0 / f64::sqrt(14.0),
        0.0
    ));
}

#[test]
fn test_magnitude_of_normal() {
    let a = tuple::Tuple::vector(1.0, 2.0, 3.0);
    assert!(approx_eq!(
        f64,
        a.normalize().magnitude(),
        1.0,
        epsilon = tuple::EPSILON
    ));
}

#[test]
fn test_dot_two_tuples() {
    let a = tuple::Tuple::vector(1.0, 2.0, 3.0);
    let b = tuple::Tuple::vector(2.0, 3.0, 4.0);
    assert!(approx_eq!(f64, a.dot(&b), 20.0, epsilon = tuple::EPSILON));
}

#[test]
fn test_cross_two_vectors() {
    let a = tuple::Tuple::vector(1.0, 2.0, 3.0);
    let b = tuple::Tuple::vector(2.0, 3.0, 4.0);
    assert!(validate_tuple(&a.cross(&b), -1.0, 2.0, -1.0, 0.0));
    assert!(validate_tuple(&b.cross(&a), 1.0, -2.0, 1.0, 0.0));
}
