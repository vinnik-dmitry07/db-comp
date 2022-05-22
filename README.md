# db-comp

A comparison of DuckDB columnar database and relational PostgreSQL.

```
DuckDB:
Count the number of goods sold: 100% | █████████████████████████████████████████████████████ | 100/100 [00:00 <00:00, 3702.83it / s]
Calculate the value of goods sold: 100% | ██████████████████████████████████████████████████ | 100/100 [00:00 <00:00, 1249.72it / s]
Calculate the value of goods sold for the period: 100% | ████████████████████████████████████ | 100/100 [00:00 <00:00, 620.98it / s]
Calculate how much of product A was purchased in store B for period C: 100% | ███████████████ | 100/100 [00:00 <00:00, 892.65it / s]
Calculate how many goods A were purchased in all stores during the period C: 100% | █████████ | 100/100 [00:00 <00:00, 900.70it / s]
Calculate the total revenue of stores for the period C: 100% | ██████████████████████████████ | 100/100 [00:00 <00:00, 624.85it / s]
Display the top 10 purchases of goods in pairs for period C (purchase> = 2 goods): 100% | ███ | 100/100 [00:00 <00:00, 107.73it / s]
Display the top 10 purchases of goods in pairs for period C (purchase == 2 goods): 100% | █████ | 100/100 [00:17 <00:00, 5.79it / s]
Display the top 10 purchases of goods in pairs for period C (purchase == 2 goods v2): 100% | █ | 100/100 [00:07 <00:00, 12.95it / s]

PostgreSQL:
Count the number of goods sold: 100% | ██████████████████████████████████████████████████████ | 100/100 [00:00 <00:00, 140.17it / s]
Calculate the value of goods sold: 100% | ████████████████████████████████████████████████████ | 100/100 [00:04 <00:00, 22.38it / s]
Calculate the value of goods sold for the period: 100% | █████████████████████████████████████ | 100/100 [00:02 <00:00, 34.39it / s]
Calculate how much of product A was purchased in store B for period C: 100% | ███████████████ | 100/100 [00:00 <00:00, 118.44it / s]
Calculate how many goods A were purchased in all stores during the period C: 100% | █████████ | 100/100 [00:00 <00:00, 116.67it / s]
Calculate the total revenue of stores for the period C: 100% | ███████████████████████████████ | 100/100 [00:02 <00:00, 34.02it / s]
Display the top 10 purchases of goods in pairs for period C (purchase> = 2 goods): 100% | ████ | 100/100 [00:04 <00:00, 21.55it / s]
Display the top 10 purchases of goods in pairs for period C (purchase == 2 goods): 100% |█████ | 100/100 [00:04 <00:00, 23.19it / s]
Display the top 10 purchases of goods in pairs for period C (purchase == 2 goods v2): 100% | ██| 100/100 [00:09 <00:00, 10.99it / s]
```