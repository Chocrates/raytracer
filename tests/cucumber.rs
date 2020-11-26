mod steps;
use async_trait::async_trait;
use raytracer::*;
use std::collections::HashMap;

use std::convert::Infallible;

pub struct MainTestWorld {
    tuples: HashMap<String, tuple::Tuple>,
}

#[async_trait(?Send)]
impl cucumber::World for MainTestWorld {
    type Error = Infallible;

    // Much more straightforward than the Default Trait before. :)
    async fn new() -> Result<Self, Infallible> {
        Ok(Self {
            tuples: HashMap::new(),
        })
    }
}

fn main() {
    // Do any setup you need to do before running the Cucumber runner.
    // e.g. setup_some_db_thing()?;
    let runner = cucumber::Cucumber::<MainTestWorld>::new()
        .features(&["./tests/features/"])
        .steps(steps::steps());

    // You may choose any executor you like (Tokio, async-std, etc)
    // You may even have an async main, it doesn't matter. The point is that
    // Cucumber is composable. :)
    futures::executor::block_on(runner.run());
}
