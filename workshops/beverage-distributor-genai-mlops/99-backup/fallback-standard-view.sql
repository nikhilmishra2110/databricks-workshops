CREATE OR REPLACE VIEW workshop.beverage_distribution.beverage_account_metrics_fallback AS
SELECT
  region,
  account_segment,
  license_status,
  reorder_risk,
  sales_rep_id,
  COUNT(DISTINCT account_id) AS account_count,
  SUM(paid_net_amount) AS paid_net_amount,
  AVG(days_since_last_paid_order) AS avg_days_since_last_order,
  SUM(CASE WHEN reorder_risk = 'high' THEN 1 ELSE 0 END) AS high_risk_accounts,
  SUM(CASE WHEN reorder_risk = 'hold' THEN 1 ELSE 0 END) AS hold_accounts
FROM workshop.beverage_distribution.gold_account_intelligence
GROUP BY
  region,
  account_segment,
  license_status,
  reorder_risk,
  sales_rep_id;

