from loguru import logger
from universal_mcp.integrations import integration
from universal_mcp.applications.yahoo_finance.app import YahooFinanceApp
from universal_mcp.applications.domain_checker import DomainCheckerApp
from universal_mcp.integrations.integration import Integration
from universal_mcp.applications.youtube.app import YoutubeApp
from universal_mcp.applications.scraper.app import ScraperApp
import asyncio
 

async def main():
    integration=Integration(name="unipile")
    # app = DomainCheckerApp(integration=None)  # type: ignore
    # result = await app.check_domain_registration("google.com")
    # app = YahooFinanceApp(integration=None)  # type: ignore
    # app = YoutubeApp(integration=integration) 
    app=ScraperApp(integration=integration)
    result = app.linkedin_people_search(keywords="software engineer")
    # result = app.get_stock_info("AAPL")
    # Basic usage - last month of daily data
    # result = app.get_stock_history("AAPL")
    
    # Different periods
    # result = app.get_stock_history("AAPL", period="1y")  # 1 year
    # result = app.get_stock_history("AAPL", period="6mo") # 6 months
    
    # Different intervals
    # result = app.get_stock_history("AAPL", period="5d", interval="1h")  # Hourly data for 5 days
    
    # Specific date range
    # result = app.get_stock_history("AAPL")
    # result = app.get_stock_news("AAPL")
    # result = app.get_financial_statements("AAPL", statement_type="cashflow")
    # result = app.get_stock_recommendations("AAPL", rec_type="upgrades_downgrades")
    # result = app.search("Boeing")
    # result = app.lookup_ticker("Apple", lookup_type="stock")
    logger.info(result)


if __name__ == "__main__":
    asyncio.run(main())