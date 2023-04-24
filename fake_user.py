"""Using fake user agent"""

from fastapi import APIRouter
from pyppeteer import launch
from fake_useragent import UserAgent

router = APIRouter()


@router.get("/")
async def main():

    proxy = '--proxy-server=hbsatya:125487dcfgawpong_country-us_session-pkus92xm_lifetime-1s@geo.iproyal.com:42324'

    user_agent = UserAgent()

    browser = await launch(
        headless=False,
        args=[f'--user-agent={user_agent.random}',
              '--no-sandbox',
              proxy
    ])
    page = await browser.newPage()

    await page.goto('https://chat.openai.com/')
