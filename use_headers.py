"""Using headers"""
from fastapi import APIRouter
from pyppeteer import launch


router = APIRouter()


@router.post('/')
async def chatgpt_scrap():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://chat.openai.com/',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://chat.openai.com/',
        'Connection': 'keep-alive',
    }

    browser = await launch(headless=False, args=['--no-sandbox'])
    page = await browser.newPage()

    await page.setExtraHTTPHeaders(headers)

    await page.goto('https://chat.openai.com')
