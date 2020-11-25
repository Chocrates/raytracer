use cucumber::{t, Steps};

pub fn steps() -> Steps<crate::MainTestWorld> {
    let mut builder: Steps<crate::MainTestWorld> = Steps::new();

    builder
        .given_regex_async(
            r#"^I have an main object initialized$"#,
            t!(|mut world, expected_texts, _step| { world }),
        )
        .when_async(
            "I call run",
            t!(|mut world, _step| {
                world.results = world.hello.run();
                world
            }),
        )
        .then_regex_async(
            r#"^I should see "([\w\s!]+)"$"#,
            t!(|world, expected_texts, _step| {
                assert_eq!(world.results, "Hello World!");
                world
            }),
        );

    builder
}
