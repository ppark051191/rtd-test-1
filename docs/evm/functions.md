## EVM Functions

***Explore and learn more about the custom functions for Sonarverse's Ethereum data share.***

### get_priced_token_activity

This function retrieves all transactions associated with a token within a specified date range. It can identify a token's transactions based on the token's address rather than its symbol, making it useful for searching tokens whose symbols are unknown to the user.

**Parameters**

| Parameter | Description |
| ----------- | ----------- |
| token_address | The address of the token being searched. |
| from_date | The start date for the date range being searched, formatted in YYYY-MM-DD. |
| to_date | The end date for the date range being searched, formatted in YYYY-MM-DD. |

**Sample Query**

After running these queries, a table will be returned. Some of the notable column definitions are outlined below.

The query below returns all the transactions of the token Uniswap using its address from March 1st, 2022, to April 2nd, 2022.

```sql
use schema ethereum_share; --change to desired chain

select *
from table(
    get_priced_token_activity(
    '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984',
    '2022-03-01',
    '2022-04-02')
);
```

### get_priced_token_activity_by_symbol

### get_priced_wallet_activity

### get_wallet_interacted_tokens

### get_wallet_profile