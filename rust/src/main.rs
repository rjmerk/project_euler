use std::time::{Instant, Duration};

mod problem_001;


fn main() {
    solve_problem(problem_001::problem_001);
}


fn solve_problem(problem: fn()) {
    let now: Instant = Instant::now();
    problem();
    let duration: Duration = now.elapsed();
    println!("Time in miliseconds: {}", duration.as_secs_f64() * 1000 as f64);
}