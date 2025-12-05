import logging

async def error_handler(update, context):
    logging.error(f"Error: {context.error}")
