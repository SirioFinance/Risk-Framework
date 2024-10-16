# Sirio Finance - Risk Framework Documentation

Sirio Finance is an innovative Lending & Borrowing protocol that, for the first time, employs a Machine Learning Model to prevent liquidation risks in a fully permissionless and arbitrary manner. This repository contains a key element of Sirio’s ecosystem: its Risk Framework. We understand that Lending & Borrowing activities carry inherent risks, both for the value of the listed tokens and for the users themselves. To address this, we have developed a comprehensive Risk Framework that accounts for a wide range of potential threats, such as Long/Short Attacks, Infinite Minting Attacks, Price Feeds Manipulation, and more. This framework aligns with the standards set by top-tier projects like Aave and Compound.

This repository includes several scripts that were used to calculate key Risk Parameters. However, it is important to note that we are still awaiting the release of public APIs from some of our providers, such as TierBot. Once these APIs are available, we will be able to fully automate the calculation process for all risk parameters. At present, the scripts in this repository allow us to obtain the following data:

## Scripts Overview

1. **PriceExtractor.py**  
   This script serves as our interface for on-chain data. In this initial version, it communicates with the Saucerswap API to retrieve the historical prices of the tokens we will list. In future updates, this file will also allow us to automatically gather additional data such as trading volumes, number of holders, token maturity days, and more.

2. **MetricsAnalyzer.py**  
   This script takes historical token prices as input and computes two types of volatility: normalized volatility, which is used to calculate the Safety Score, and Parkinson Volatility, normalized to a value scale that is suited for calculating the Loan-To-Value (LTV) ratio using the formula proposed by RiskDAO in Aave's governance.

3. **TokenPctQty.py**  
   This script is essential for calculating the Supply Cap. One of the key conditions for defining the maximum borrowable/lendable amount in a given market is that it must not exceed the quantity required to move the token's price by 25%.

## Future Developments
We are continuously improving the Risk Framework to better manage risk and secure our users’ assets. The full automation of risk parameter calculations, supported by additional data sources, will significantly enhance the accuracy and reliability of our protocol’s risk management strategies.

The upcoming updates to this repository will include:
1. Integration of the TierBot APIs
2. Full automation in the calculation of Final Risk Parameters
3. Integration of an Open-Source Dashboard that will display real-time Risk Parameters for each token, including active loans and their associated Liquidation Risks

For any feedback or contributions, feel free to open an issue or submit a pull request.

