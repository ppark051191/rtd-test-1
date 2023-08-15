# Cross Chain Share

Explore and learn about the custom functions for Sonarverse's cross-chain data share.

### get_priced_token_activity_by_symbol

This function returns every transaction a token engages in between the given dates. It can find the given token's transactions using the token's symbol instead of the token's address.

**Parameter**

| Parameter | Description |
| ----------- | ----------- |
| symbol | The symbol of the token being searched. |
| from_date | The start date for the date range being searched, formatted in YYYY-MM-DD. |
| to_date | The end date for the date range being searched, formatted in YYYY-MM-DD. |

**Sample Query**

After running this query, a table will be returned. Some of the notable column definitions are outlined in the following section.

The query below returns all the transactions of the token Uniswap using its symbol from March 1st, 2022, to April 2nd, 2022.

```sql
use schema cross_chain_share;

select *
from table(
    get_priced_token_activity_by_symbol(
    'uni',
    '2022-03-01',
    '2022-04-02')
);
```

**Notable column details**

| Column | Description |
| ----------- | ----------- |
| CHAIN | The supported chain for cross-chain analysis. |
| VALUE | The curated quantity of the token. A negative value indicates the token is being sent out. A positive value indicates that a token is being received. |
| USD_VALUE | The USD value of the entire transaction at the time of the transaction. (historical pricing) |
| CURRENT_USD_VALUE | The USD value of the transaction at the time of the query. (live pricing) |

### get_priced_wallet_activity

This function returns all token activity in a wallet between the given dates. This function can be used to ensure a wallet is trustworthy prior to interacting with it.

**Parameter**

| Parameter | Description |
| ----------- | ----------- |
| wallet_address | The address of the wallet being searched. |
| from_date | The start date for the date range being searched, formatted in YYYY-MM-DD. |
| to_date | The end date for the date range being searched, formatted in YYYY-MM-DD. |

**Sample Query**

After running these queries, a table will be returned. Some of the notable column definitions are outlined in the following section.

The query below returns all token activity in a wallet using its address from February 1st, 2022, to April 2nd, 2022, in descending order by date.

```sql
use schema cross_chain_share; --change to desired chain

select *
from table(
    get_priced_wallet_activity(
    '0x4862733B5FdDFd35f35ea8CCf08F5045e57388B3',
    '2022-02-01',
    '2022-04-02')
)
order by datetime desc;
```

The query below returns the USD value of all unique tokens in a wallet from February 1st, 2022, to April 2nd, 2022.

```sql
use schema cross_chain_share; --change to desired chain

select
    chain,
    sum(usd_value) as total_usd_value
from table(
    get_priced_wallet_activity(
    '0x4862733b5fddfd35f35ea8ccf08f5045e57388b3',
    '2022-02-01',
    '2022-04-02')
)
group by chain;
```

**Notable column details**

| Column | Description |
| ----------- | ----------- |
| CHAIN | The supported chain for cross-chain analysis. |
| SYMBOL | The symbol of the token being searched. |

### get_wallet_profile

This function returns an aggregation of key wallet metrics and the total USD volume of all transactions in a specified wallet since its inception. Numerous use cases for this function encompass personal performance tracking and tax reporting, among others.

**Parameter**

| Parameter | Description |
| ----------- | ----------- |
| wallet_address | The address of the wallet being searched. |

**Sample Query**

After running this query, a table will be returned. Some of the notable column definitions are outlined in the following section.

The query below returns all interactions in a wallet using its address from its creation to the present day.

```sql
use schema cross_chain_share; --change to desired chain

select *
from table(
    get_wallet_profile(
    '0x2a65aca4d5fc5b5c859090a6c34d164135398226')
);
```

**Notable column details**

| Column | Description |
| ----------- | ----------- |
| START_DATE | The creation date of the wallet. |
| NUMBER_OF_TRANSFERS | The total number of transfers a wallet has engaged in. |
| TOTAL_USD_VOLUME | The USD value of all transactions in the wallet since it's creation.  |
| CHAIN | The supported chain for cross-chain analysis. |
