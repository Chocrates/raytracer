use cucumber::{t, Steps};
use std::fmt;
use raytracer::*;

pub fn steps() -> Steps<crate::MainTestWorld> {
    let mut builder: Steps<crate::MainTestWorld> = Steps::new();

    builder
        .given_regex_async(
            r#"^([a-z]) ← tuple\(([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*)\)$"#,
            t!(|mut world, _match, _step| { 
                world.tuples.insert(format!("{}", _match[1]), tuple::Tuple::new(_match[2].parse::<f64>().unwrap(), _match[3].parse::<f64>().unwrap(), _match[4].parse::<f64>().unwrap(), _match[5].parse::<f64>().unwrap()));
                world 
            }),
        )
        .given_regex_async(
            r#"^([a-z]) ← point\(([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*)\)$"#,
            t!(|mut world, matches, _step| {
                println!("{}", matches[0]);
                println!("{}", matches[1]);
                println!("{}", matches[2]);
                println!("{}", matches[3]);
                world.tuples.insert(format!("{}", matches[1]), tuple::Tuple::point(matches[2].parse::<f64>().unwrap(), matches[3].parse::<f64>().unwrap(), matches[4].parse::<f64>().unwrap()));
                world
            }),
        )
        .given_regex_async(
            r#"^([a-z]) ← vector\(([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*)\)$"#,
            t!(|mut world, matches, _step| {
                world.tuples.insert(format!("{}", matches[1]), tuple::Tuple::vector(matches[2].parse::<f64>().unwrap(), matches[3].parse::<f64>().unwrap(), matches[4].parse::<f64>().unwrap()));
                world
            }),
        )
        .then_regex_async(
            r#"^([a-z])\.([xyzw]) = ([-+]?[0-9]*\.?[0-9]*)$"#,
            t!(|world, matches, _step| { 
                assert!(world.tuples.contains_key(&matches[1]));
                if matches[2] == "x" {
                    assert_eq!(world.tuples.get(&matches[1]).unwrap().x,
                            matches[3].parse::<f64>().unwrap());
                } else if matches[2] == "y" {
                    assert_eq!(world.tuples.get(&matches[1]).unwrap().y,
                            matches[3].parse::<f64>().unwrap());
                } else if matches[2] == "z" {
                    assert_eq!(world.tuples.get(&matches[1]).unwrap().z,
                            matches[3].parse::<f64>().unwrap());
                } else if matches[2] == "w" {
                    assert_eq!(world.tuples.get(&matches[1]).unwrap().w,
                            matches[3].parse::<f64>().unwrap());
                } else {
                    println!("{}", matches[0]);
                    println!("{}", matches[1]);
                    println!("{}", matches[2]);
                    println!("{}", matches[3]);
                    assert!(false, "Unknown tuple attribute");
                }
                world 
            }),
        )
        .then_regex_async(
            r#"^([a-z]) is not a vector$"#,
            t!(|world, matches, _step| { 
                assert!(world.tuples.contains_key(&matches[1]));
                assert_eq!(world.tuples.get(&matches[1]).unwrap().is_vector(),
                        false);
                world
            }),
        )
        .then_regex_async(
            r#"^([a-z]) is a vector$"#,
            t!(|world, matches, _step| { 
                assert!(world.tuples.contains_key(&matches[1]));
                assert_eq!(world.tuples.get(&matches[1]).unwrap().is_vector(),
                        true);
                world
            }),
        )
        .then_regex_async(
            r#"^([a-z]) is not a point$"#,
            t!(|world, matches, _step| { 
                assert!(world.tuples.contains_key(&matches[1]));
                assert_eq!(world.tuples.get(&matches[1]).unwrap().is_point(),
                        false);
                world
            }),
        )
        .then_regex_async(
            r#"^([a-z]) is a point$"#,
            t!(|world, matches, _step| { 
                assert!(world.tuples.contains_key(&matches[1]));
                assert_eq!(world.tuples.get(&matches[1]).unwrap().is_point(),
                        true);
                world
            }),
        )
        .then_regex_async(
            r#"^([a-z]) = tuple\(([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*), ([-+]?[0-9]*\.?[0-9]*)\)$"#,
            t!(|world, matches, _step| { 
                assert!(world.tuples.contains_key(&matches[1]));
                assert_eq!(world.tuples.get(&matches[1]).unwrap().x, matches[2].parse::<f64>().unwrap());
                assert_eq!(world.tuples.get(&matches[1]).unwrap().y, matches[3].parse::<f64>().unwrap());
                assert_eq!(world.tuples.get(&matches[1]).unwrap().z, matches[4].parse::<f64>().unwrap());
                assert_eq!(world.tuples.get(&matches[1]).unwrap().w, matches[5].parse::<f64>().unwrap());
                
                world
            }),
        );

    builder
}
