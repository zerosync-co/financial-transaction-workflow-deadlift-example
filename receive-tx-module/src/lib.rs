use chrono::{DateTime, Utc};
use extism_pdk::*;
use serde::Deserialize;
use serde_json::Value;

#[derive(Debug, Deserialize)]
struct FinancialTransaction {
    transaction_id: i32,
    timestamp: DateTime<Utc>,
    amount: f32,
    currency: String,
    sender_account_id: i32,
    receiver_account_id: i32,
}

#[plugin_fn]
pub fn _main(Json(tx): Json<FinancialTransaction>) -> FnResult<Value> {
    info!("{tx:?}");
    Ok(Value::default())
}
