use super::common::*;

// Import catchamouse16 functions
use crate::catchamouse16::sy_driftingmean::sy_driftingmean50_min;
use crate::catchamouse16::sy_slidingwindow::sy_slidingwindow;
use crate::catchamouse16::st_localextrema::st_localextrema_n100_diffmaxabsmin;

/// SY_DriftingMean50_Min feature
pub struct SYDriftingMean50Min;
impl FeatureCompute for SYDriftingMean50Min {
    fn compute(&self, y: &[f64], _normalize: bool) -> f64 {
        sy_driftingmean50_min(y)
    }
    fn name(&self) -> String {
        "sy_driftingmean50_min".to_string()
    }
}

/// SY_SlidingWindow with std/std parameters
pub struct SYSlidingWindowStdStd {
    pub num_seg: usize,
    pub inc_move: usize,
}

impl Default for SYSlidingWindowStdStd {
    fn default() -> Self {
        Self {
            num_seg: 5,
            inc_move: 2,
        }
    }
}

impl FeatureCompute for SYSlidingWindowStdStd {
    fn compute(&self, y: &[f64], _normalize: bool) -> f64 {
        sy_slidingwindow(y, "std", "std", self.num_seg, self.inc_move)
    }
    fn name(&self) -> String {
        format!("sy_slidingwindow_std_std_{}_{}", self.num_seg, self.inc_move)
    }
}

/// SY_SlidingWindow with mean/std parameters  
pub struct SYSlidingWindowMeanStd {
    pub num_seg: usize,
    pub inc_move: usize,
}

impl Default for SYSlidingWindowMeanStd {
    fn default() -> Self {
        Self {
            num_seg: 5,
            inc_move: 2,
        }
    }
}

impl FeatureCompute for SYSlidingWindowMeanStd {
    fn compute(&self, y: &[f64], _normalize: bool) -> f64 {
        sy_slidingwindow(y, "mean", "std", self.num_seg, self.inc_move)
    }
    fn name(&self) -> String {
        format!("sy_slidingwindow_mean_std_{}_{}", self.num_seg, self.inc_move)
    }
}

/// ST_LocalExtrema_N100_DiffMaxAbsMin feature
pub struct STLocalExtremaN100DiffMaxAbsMin;
impl FeatureCompute for STLocalExtremaN100DiffMaxAbsMin {
    fn compute(&self, y: &[f64], _normalize: bool) -> f64 {
        st_localextrema_n100_diffmaxabsmin(y)
    }
    fn name(&self) -> String {
        "st_localextrema_n100_diffmaxabsmin".to_string()
    }
}

pub type Catchamouse16Output = FeatureOutput;

/// Compute all Catchamouse16 features in parallel
pub fn compute_catchamouse16_parallel(y: Vec<f64>, normalize: bool) -> Catchamouse16Output {
    let features: Vec<Box<dyn FeatureCompute>> = vec![
        Box::new(SYDriftingMean50Min),
        Box::new(SYSlidingWindowStdStd::default()),
        Box::new(SYSlidingWindowMeanStd::default()),
        Box::new(STLocalExtremaN100DiffMaxAbsMin),
    ];

    compute_features_parallel_dyn(y, normalize, features)
}

/// Extract Catchamouse16 features cumulatively
pub fn extract_catchamouse16_features_cumulative_optimized(
    series: &[f64],
    normalize: bool,
    value_column_name: Option<&str>,
) -> CumulativeResult {
    extract_features_cumulative_optimized(
        series,
        normalize,
        value_column_name,
        |data, norm| compute_catchamouse16_parallel(data.to_vec(), norm),
    )
}