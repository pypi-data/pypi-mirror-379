import pandas as pd
from typing import Optional, List, Union
import finnhub
import os

class FundamentalIndicators:
    """
    Fetches fundamental financial data, ratios, and insider sentiment for given stock tickers.
    
    This class is a wrapper around Finnhub API, but users interact only via AlphaBuilder's interface.
    Users provide their API key via the environment variable `ALPHABUILDER_API_KEY` 
    or via the `api_key` argument.
    
    Attributes
    ----------
    tickers : List[str]
        List of stock tickers to fetch data for.
    start_date : str
        Start date for filtering data (format 'YYYY-MM-DD').
    end_date : Optional[str]
        End date for filtering data (format 'YYYY-MM-DD').
    verbose : bool
        If True, prints progress messages.
    combined : bool
        If True, returns a single concatenated DataFrame for all tickers.
    data : Union[pd.DataFrame, dict]
        Stores the last fetched data.
    client : finnhub.Client
        Hidden Finnhub client instance.
    """
    def __init__(
        self,
        tickers: Optional[List[str]] = None, 
        start_date: str = "2010-01-01",
        end_date: Optional[str] = None,
        verbose: bool = True,
        combined: bool = False,
        api_key: Optional[str] = None
    ):
        """
        Parameters
        ----------
        tickers : Optional[List[str]]
            Stock tickers to fetch data for. Defaults to ['AAPL'].
        start_date : str
            Filter data starting from this date.
        end_date : Optional[str]
            Filter data up to this date.
        verbose : bool
            If True, prints fetching progress.
        combined : bool
            If True, returns a single DataFrame combining all tickers.
        api_key : Optional[str]
            AlphaBuilder API key (hidden Finnhub key). 
            Can also be set via environment variable 'ALPHABUILDER_API_KEY'.
        """
        self.tickers = tickers or ["AAPL"] 
        self.start_date = start_date
        self.end_date = end_date
        self.verbose = verbose
        self.combined = combined
        self.data: Union[pd.DataFrame, dict] = {}
        
        api_key = api_key or os.getenv("ALPHABUILDER_API_KEY")
        if api_key is None:
            raise ValueError(
                "Please provide a Finnhub API key via the `api_key` argument "
                "or set the environment variable 'FINNHUB_API_KEY'.\n"
                "You can get a free Finnhub key here: https://finnhub.io/register"
            )
            
        self.client = finnhub.Client(api_key=api_key)

    def company_financial_ratios(self, series = "annual"):
        """
        Fetches basic financial ratios (P/E, ROE, Debt/Equity, etc.) for the tickers.
        
        Parameters
        ----------
        series : str
            'annual' or 'quarterly' ratios to fetch.
        
        Returns
        -------
        dict or pd.DataFrame
            Dictionary of DataFrames per ticker, or a single DataFrame if combined=True.
            Multi-indexed by ('symbol', 'period') with ratio names as columns.
        """
        if series.lower() not in ["annual", "quarterly"]:
            raise ValueError("series must be 'annual' or 'quarterly'")
        all_data = {}

        for symbol in self.tickers:
            if self.verbose:
                print(f"Fetching financial ratios for {symbol}...")

            fin_financial_data = self.client.company_basic_financials(symbol, 'all')
            records = []

            for key, values in fin_financial_data.get("series", {}).get(series, {}).items():
                for item in values:
                    records.append({
                        "symbol": fin_financial_data.get("symbol", symbol),
                        "indicator": key,
                        "period": item.get("period"),
                        "value": item.get("v")
                    })

            df = pd.DataFrame(records)

            df['period'] = pd.to_datetime(df['period'])

            if self.start_date:
                start_date = pd.to_datetime(self.start_date)
            else:
                start_date = None
                
            if self.end_date:
                end_date = pd.to_datetime(self.end_date)
            else:
                end_date = None

            if start_date is not None:
                df = df[df['period'] >= start_date]
            if end_date is not None:
                df = df[df['period'] <= end_date]

            df = df.reset_index(drop=True)

            df_pivot = df.pivot(index=['symbol', 'period'], columns='indicator', values='value')
            df_pivot = df_pivot.sort_index()  
            df_pivot.columns.name = None

            all_data[symbol] = df_pivot

        if self.combined:
            self.data = pd.concat(all_data.values()).sort_index()
        else:
            self.data = all_data

        return self.data
    
    def company_financial_reported(self, series="annual"):
        """
        Fetches GAAP financial reports (Balance Sheet, Income Statement, Cash Flow) for tickers.
        
        Parameters
        ----------
        series : str
            'annual' or 'quarterly' filings.
        
        Returns
        -------
        dict or pd.DataFrame
            Dictionary of DataFrames per ticker or combined DataFrame if combined=True.
            Multi-indexed by ('symbol', 'endDate', 'quarter') with MultiIndex columns ('section', 'concept').
        """
        all_data = {}
        
        if series.lower() not in ["annual", "quarterly"]:
            raise ValueError("series should be either annual or quarterly")
        
        for symbol in self.tickers:
            if self.verbose:
                print(f"Fetching GAAP financial report for {symbol}...")
                
            start_date = pd.to_datetime(self.start_date)
            end_date = pd.to_datetime(self.end_date)
            
            fin_company_data = self.client.financials_reported(symbol=symbol, freq=series)
            rows = []
            
            for filing in fin_company_data.get("data", []):
                end_date_filing = pd.to_datetime(filing["endDate"])
                
                if start_date and end_date_filing < start_date:
                    continue
                if end_date and end_date_filing > end_date:
                    continue

                for section, values in filing["report"].items():
                    row = {
                        "symbol": filing["symbol"],
                        "year": filing["year"],
                        "quarter": filing["quarter"],
                        "form": filing["form"],
                        "startDate": filing["startDate"],
                        "endDate": filing["endDate"],
                        "filedDate": filing.get("filedDate"),
                        "section": section
                    }

                    if isinstance(values, dict):
                        row.update(values)
                        rows.append(row)

                    elif isinstance(values, list):
                        for item in values:
                            subrow = row.copy()
                            subrow.update(item)
                            rows.append(subrow)

            df = pd.DataFrame(rows)
            columns = ['startDate', 'filedDate', 'label', 'form', 'year', 'unit']
            df.drop(columns=columns, inplace=True, errors='ignore')
            df["endDate"] = pd.to_datetime(df["endDate"], errors='coerce').dt.date
            df_pivot = df.pivot_table(
                index=["symbol", "endDate", "quarter"], 
                columns=["section", "concept"], 
                values="value", 
                aggfunc="first" 
                ).sort_index()
            
            df_pivot.columns.name = None
            df_pivot.columns = [f"{sec}_{con}" for sec, con in df_pivot.columns]
            
            pd.set_option('display.float_format', '{:,.0f}'.format)
            all_data[symbol] = df_pivot

        if self.combined:
            self.data = pd.concat(all_data.values()).sort_index()
        else:
            self.data = all_data
            
        return self.data
    
    def company_insider_sentiments(self):
        """
        Fetches insider sentiment data for the tickers.
        
        Returns
        -------
        dict or pd.DataFrame
            Dictionary of DataFrames per ticker or combined DataFrame if combined=True.
            Multi-indexed by ('symbol', 'period') with columns ['change', 'mspr'].
        """
        all_data = {}

        for symbol in self.tickers:
            if self.verbose:
                print(f"Fetching insider sentiment for {symbol}...")

            fin_insider_sentiment = self.client.stock_insider_sentiment(
                symbol,
                self.start_date,
                self.end_date
            )

            records = []
            for item in fin_insider_sentiment.get("data", []):
                period = pd.to_datetime(f"{item['year']}-{item['month']:02d}-01")
                records.append({
                    "symbol": fin_insider_sentiment.get("symbol", symbol),
                    "period": period,
                    "change": item.get("change"),
                    "mspr": item.get("mspr")
                })

            df = pd.DataFrame(records)
            df = df.reset_index(drop=True)
            df_pivot = df.set_index(["symbol", "period"])[["change", "mspr"]]
            df_pivot = df_pivot.sort_index()

            all_data[symbol] = df_pivot

        if self.combined:
            self.data = pd.concat(all_data.values()).sort_index()
        else:
            self.data = all_data

        return self.data