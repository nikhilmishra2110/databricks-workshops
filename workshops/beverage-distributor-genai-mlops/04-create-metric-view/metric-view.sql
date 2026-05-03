CREATE OR REPLACE VIEW workshop.beverage_distribution.beverage_account_metrics
WITH METRICS
LANGUAGE YAML
AS $$
version: 1.1
comment: "Business metrics for beverage distribution account intelligence."
source: workshop.beverage_distribution.gold_account_intelligence

dimensions:
  - name: account_id
    expr: account_id
    display_name: "Account ID"
    comment: "Synthetic account identifier."
  - name: account_name
    expr: account_name
    display_name: "Account Name"
    comment: "Synthetic account name."
  - name: region
    expr: region
    display_name: "Region"
    comment: "Sales region."
    synonyms: ["territory", "market"]
  - name: account_segment
    expr: account_segment
    display_name: "Account Segment"
    comment: "Type of account such as grocery, restaurant, retail, or hospitality."
  - name: license_status
    expr: license_status
    display_name: "License Status"
    comment: "Whether the account can receive product orders."
  - name: reorder_risk
    expr: reorder_risk
    display_name: "Reorder Risk"
    comment: "Estimated risk that the account needs reorder follow-up."
    synonyms: ["account risk", "follow-up risk"]
  - name: sales_rep_id
    expr: sales_rep_id
    display_name: "Sales Rep"
    comment: "Synthetic field sales representative identifier."

measures:
  - name: account_count
    expr: COUNT(DISTINCT account_id)
    display_name: "Account Count"
    comment: "Number of distinct accounts."
  - name: paid_net_amount
    expr: SUM(paid_net_amount)
    display_name: "Paid Net Amount"
    comment: "Total paid net order amount."
    synonyms: ["sales", "net sales", "revenue"]
  - name: avg_days_since_last_order
    expr: AVG(days_since_last_paid_order)
    display_name: "Average Days Since Last Order"
    comment: "Average days since the last paid order."
  - name: high_risk_accounts
    expr: SUM(CASE WHEN reorder_risk = 'high' THEN 1 ELSE 0 END)
    display_name: "High Risk Accounts"
    comment: "Accounts classified as high reorder risk."
  - name: hold_accounts
    expr: SUM(CASE WHEN reorder_risk = 'hold' THEN 1 ELSE 0 END)
    display_name: "Hold Accounts"
    comment: "Accounts that should be held because of license or compliance status."
$$;

