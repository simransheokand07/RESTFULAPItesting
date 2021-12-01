import pandas as pd
from allapi_test_fetchdata.py import *

endpoint = ["https://data.sifchain.finance/beta/pool",
            "https://data.sifchain.finance/beta/pool/1inch",
            "https://data.sifchain.finance/beta/pool/1inch/liquidityProvider",
            "https://data.sifchain.finance/beta/pool/1inch/liquidityProvider/sif10c8znaj94y900syues06dz50hw6y9qpk3jgkmc",
            "https://data.sifchain.finance/beta/pool/1inch/liquidityProvider/sif10c8znaj94y900syues06dz50hw6y9qpk3jgkmc/share",
            "https://data.sifchain.finance/beta/validator",
            "https://data.sifchain.finance/beta/validator/sifvaloper1qwn3usp82ux4va5kdjfnak4v0dnhg3gj3qa490",
            "https://data.sifchain.finance/beta/validator/sifvaloper1qwn3usp82ux4va5kdjfnak4v0dnhg3gj3qa490/delegator",
            "https://data.sifchain.finance/beta/validator/delegator/sif1qrxylp97p25wcqn4cs9nd02v672073ynpkt4yr",
            "https://data.sifchain.finance/beta/validator/inactiveValidators",
            "https://data.sifchain.finance/beta/validator/delegator/totalStaked",
            "https://data.sifchain.finance/beta/asset",
            "https://data.sifchain.finance/beta/asset/1inch",
            "https://data.sifchain.finance/beta/asset/tokenStats",
            "https://data.sifchain.finance/beta/network",
            "https://data.sifchain.finance/beta/network/dispensation/lm_bonus",
            "https://data.sifchain.finance/beta/dailyPrice",
            "https://data.sifchain.finance/beta/cmcTotalDailyVolume",
            "https://data.sifchain.finance/beta/historicalPrice/1inch",
            "https://data.sifchain.finance/beta/summary",
            "https://data.sifchain.finance/beta/validator/stakingRewards",
            "https://data.sifchain.finance/beta/asset/totalSupply",
            "https://data.sifchain.finance/beta/asset/cmcTotalSupply",
            "https://data.sifchain.finance/beta/asset/circulatingsupply",
            "https://data.sifchain.finance/beta/asset/cmcCirculatingSupply",
            "https://data.sifchain.finance/beta/trade/eth_usdt"
            ]

df = pd.DataFrame(endpoint)
df.to_csv('allapi_symbolslist.csv', index=False)
print(df)
