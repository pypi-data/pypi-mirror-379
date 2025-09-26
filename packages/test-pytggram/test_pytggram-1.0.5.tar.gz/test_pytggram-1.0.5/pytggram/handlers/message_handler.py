from .handler import Handler
from ..types import Message

class MessageHandler(Handler):
    """Handler for message updates"""
    def __init__(self, callback, filters=None, group=0):
        super().__init__(callback, filters, group)
    
    async def handle(self, client, update: dict):
        """Handle a message update"""
        try:
            message_data = update.get('message', {})
            if not message_data:
                return
                
            message = Message.from_dict(message_data)
            if self.check(message):
                await self.callback(client, message)
        except Exception as e:
            import logging
            logger = logging.getLogger('pytggram')
            logger.error(f"Error in message handler: {e}")
