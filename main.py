import asyncio

from dotenv import load_dotenv
load_dotenv(".env")
from src.app import main

if __name__ == '__main__':
    asyncio.run(main())