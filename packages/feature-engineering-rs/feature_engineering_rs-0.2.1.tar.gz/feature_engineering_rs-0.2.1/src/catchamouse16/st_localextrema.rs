use crate::helpers::common::{min_f, max_f};

pub fn st_localextrema_n100_diffmaxabsmin(y: &[f64]) -> f64 {
    let num_windows = 100;
    let wl = y.len() / num_windows;

    if y.len() < num_windows {
        // For short time series, use the entire series as one window
        let locmax = max_f(y, None);
        let abslocmin = min_f(y, None).abs();
        return (locmax - abslocmin).abs();
    }
    
    if wl <= 1 {
        eprintln!("Error in ST_LocalExtrema: window length less than 1 or greater than ts");
        eprintln!("Couldn't divide the time series into multiple windows");
        return f64::NAN;
    }

    // Dividing the ts into windows
    let mut y_buff = Vec::with_capacity(num_windows);
    for i in 0..num_windows {
        let mut window = Vec::with_capacity(wl);
        for j in 0..wl {
            if i * wl + j < y.len() {
                window.push(y[i * wl + j]);
            } else {
                window.push(0.0);
            }
        }
        y_buff.push(window);
    }

    // If last window is all zero then remove it
    let mut num_windows = num_windows;
    if let Some(last_window) = y_buff.last() {
        if last_window.iter().all(|&x| x == 0.0) {
            num_windows -= 1;
        }
    }

    // Find Local Extrema
    let mut diffmaxabsmin = 0.0;
    for i in 0..num_windows {
        let locmax = max_f(&y_buff[i], None);
        let abslocmin = min_f(&y_buff[i], None).abs();
        diffmaxabsmin += (locmax - abslocmin).abs();
    }
    diffmaxabsmin / num_windows as f64
}