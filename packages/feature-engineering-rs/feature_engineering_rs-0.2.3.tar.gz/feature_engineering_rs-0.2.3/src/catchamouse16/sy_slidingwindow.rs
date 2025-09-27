use crate::helpers::common::{mean_f, stdev_f};

pub fn sy_slidingwindow(y: &[f64], window_stat: &str, across_win_stat: &str, num_seg: usize, inc_move: usize) -> f64 {
    // NAN check
    if y.iter().any(|&val| val.is_nan()) {
        return f64::NAN;
    }

    let size = y.len();
    let winlen = size / num_seg;
    let mut inc = winlen / inc_move;
    if inc == 0 {
        inc = 1;
    }

    let num_steps = (size - winlen) / inc + 1;
    let mut qs = Vec::with_capacity(num_steps);

    match window_stat {
        "mean" => {
            for i in 0..num_steps {
                let start_idx = i * inc;
                let end_idx = start_idx + winlen;
                let window_slice = &y[start_idx..end_idx];
                qs.push(mean_f(window_slice));
            }
        }
        "std" => {
            for i in 0..num_steps {
                let start_idx = i * inc;
                let end_idx = start_idx + winlen;
                let window_slice = &y[start_idx..end_idx];
                qs.push(stdev_f(window_slice, 1)); // ddof=1 for sample std
            }
        }
        _ => {
            eprintln!("Error in sy_slidingwindow: Unknown window statistic!");
            return f64::NAN;
        }
    }

    // NAN check on computed statistics
    if qs.iter().any(|&val| val.is_nan()) {
        return f64::NAN;
    }

    match across_win_stat {
        "std" => {
            let qs_std = stdev_f(&qs, 1);
            let y_std = stdev_f(y, 1);
            qs_std / y_std
        }
        _ => {
            eprintln!("Error in sy_slidingwindow: Unknown across-window statistic!");
            f64::NAN
        }
    }
}