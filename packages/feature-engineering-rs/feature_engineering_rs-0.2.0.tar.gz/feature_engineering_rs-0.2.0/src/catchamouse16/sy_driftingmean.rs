use crate::helpers::common::{mean_f, min_f};

pub fn sy_driftingmean50_min(y: &[f64]) -> f64 {
    
    if y.iter().any(|&val| val.is_nan()) {
        return f64::NAN;
    }

    let l = 50;
    let numfits = y.len() / l;
    
    if numfits == 0 {
        return f64::NAN;
    }
    
    // Create segments of length l
    let mut z: Vec<Vec<f64>> = Vec::with_capacity(numfits);
    for i in 0..numfits {
        let start = i * l;
        let end = start + l;
        z.push(y[start..end].to_vec());
    }
    
    // Calculate mean and variance for each segment
    let mut zm: Vec<f64> = Vec::with_capacity(numfits);
    let mut zv: Vec<f64> = Vec::with_capacity(numfits);
    
    for segment in &z {
        let segment_mean = mean_f(segment);
        zm.push(segment_mean);
        
        // Calculate variance manually (like in stdev_f but without sqrt)
        let variance = segment.iter()
            .map(|&value| (value - segment_mean).powi(2))
            .sum::<f64>() / (segment.len() - 1) as f64;
        zv.push(variance);
    }
    
    let meanvar = mean_f(&zv);
    let minmean = min_f(&zm, None);
    
    minmean / meanvar
}